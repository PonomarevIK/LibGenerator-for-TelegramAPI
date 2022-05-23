from keyword import iskeyword

API_URL = "https://api.telegram.org/bot{token}/{method}"


class BaseObject:
    def __init__(self, name, description, parameters):
        self.name = name
        self.description = description
        self.parameters = parameters


class BaseMethod(BaseObject):
    def __init__(self, name, description, parameters):
        super().__init__(name, description, parameters)
        self.return_type = self.get_return_type()

    def get_return_type(self) -> str:
        return_type = "{}"
        possible_types = []
        for sentence in self.description.split("."):
            if "error" in sentence:
                continue
            if "return" in sentence.lower():
                for word in sentence.split()[1:]:
                    if word.lower() == "array":
                        return_type = "[" + return_type + "]"
                    elif word == "True":
                        possible_types.append("Boolean")
                    elif word and word[0].isupper():
                        possible_types.append(word.removesuffix("s") if ("[" in return_type) else word)
        return return_type.format(" or ".join(possible_types))


class PythonObjectWriter(BaseObject):
    replacements = {
        " or ": " | ",
        "[": "list[",
        "Boolean": "bool",
        "Integer": "int",
        "Int": "int",
        "Float": "float",
        "String": "str"}

    def __init__(self, name, description, parameters):
        super().__init__(name, description, parameters)
        self.pythonify_parameters()

    def pythonify_parameters(self):
        for i, parameter in enumerate(self.parameters):
            if iskeyword(parameter["name"]):
                self.parameters[i]["name"] += "_"
            for old, new in self.replacements.items():
                self.parameters[i]["type"] = self.parameters[i]["type"].replace(old, new)

    def get_argument_list(self):
        return ["{name}: {type}".format(**param) for param in self.parameters if not param["is_optional"]] + \
               ["{name}: {type} = None".format(**param) for param in self.parameters if param["is_optional"]]


class PythonMethodWriter(PythonObjectWriter, BaseMethod):
    header = ("import requests\n",
              "from types import *\n\n",
              f"API_URL = {API_URL}\n"
              "token = 'your_bot_token_here'\n")

    def __init__(self, name, description, parameters):
        super().__init__(name, description, parameters)
        self.payload = "\n    ".join(self.payload_generator())
        self.pythonify_return_type()

    def pythonify_return_type(self):
        for old, new in self.replacements.items():
            self.return_type = self.return_type.replace(old, new)

    def payload_generator(self):
        for parameter in self.parameters:
            if parameter["is_optional"]:
                yield "if {name} is not None:\n        payload['{name}'] = {name}".format(**parameter)
            else:
                yield "payload['{name}'] = {name}".format(**parameter)
