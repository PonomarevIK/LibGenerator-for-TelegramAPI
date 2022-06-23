from keyword import iskeyword
from base_code_generator import *


class PythonObjectWriter(BaseObject):
    template_path = "Templates/Python/type_template.txt"
    replacements = {
        " or ": " | ",
        "[": "list[",
        "Boolean": "bool",
        "True": "bool",
        "Integer": "int",
        "Int": "int",
        "Float": "float",
        "String": "str",
        "Null": "None", }
    header = "# This code in its entirety was generated and formatted automatically\n\n"

    with open(template_path, "r", encoding="unicode_escape") as template_file:
        template = template_file.read()

    def __init__(self, name, description, parameters):
        super().__init__(name, description, parameters)
        self.pythonify_parameters()

    def pythonify_parameters(self):
        """Replaces parameter names and types with their python version

        from: User -> from_: User  (from is a python keyword)
        text: String -> text: str
        """
        for i, parameter in enumerate(self.parameters):
            if iskeyword(parameter["name"]):
                self.parameters[i]["name"] += "_"
            for old, new in self.replacements.items():
                if old in self.parameters[i]["type"]:
                    self.parameters[i]["type"] = self.parameters[i]["type"].replace(old, new)

    def docstring_generator(self, field_type):
        """Generates a docstring for each object/method with every attribute/parameter line by line"""
        yield self.description
        yield from (":{ft} {name}: {description}".format(ft=field_type, **param) for param in self.parameters)

    def init_generator(self):
        """Generated __init__ method for each object line by line

        user_id: int -> self.user_id = int(json["id"])
        username: str = None -> \
        if "username" in json:
            self.username = str(json["username"])
        """
        for attr in self.parameters:
            line = "self.{name} = ".format(**attr)
            if attr["type"].startswith("list[list["):
                line += "[[{type}(item) for item in arr] for arr in json['{name}']]"
            elif attr["type"].startswith("list["):
                line += "[{type}(item) for item in json['{name}']]"
            else:
                line += "{type}(json['{name}'])"
            if attr["is_optional"]:
                line = f"if '{{name}}' in json:\n            " + line
            yield line.format(name=attr["name"].removesuffix("_"), type=attr["type"])

    @classmethod
    def write_file_header(cls, path):
        with open(path, "w", encoding="utf-8") as output_file:
            output_file.write(cls.header)

    def write_to_file(self, path):
        with open(path, "a", encoding="utf-8") as output_file:
            output_file.write(self.template.format(name=self.name,
                                                   description="\n    ".join(self.docstring_generator("attribute")),
                                                   init=f"\n        ".join(self.init_generator())))
            output_file.write("\n\n")


class PythonMethodWriter(PythonObjectWriter, BaseMethod):
    template_path = "Templates/Python/method_template.txt"
    header = ("# This code in its entirety was generated and formatted automatically\n\n"
              "import requests\n"
              "from types import *\n\n"
              f"API_URL = '{API_URL}'\n"
              "token = 'your_bot_token_here'\n"
              "logger = None\n"
              "\n\n")

    with open(template_path, "r", encoding="unicode_escape") as template_file:
        template = template_file.read()

    def __init__(self, name, description, parameters):
        super().__init__(name, description, parameters)
        self.pythonify_return_type()

    def parameter_generator(self):
        """Generates a sequence of parameters with default values for optional parameters"""
        yield from ("{name}: {type}".format(**param) for param in self.parameters if not param["is_optional"])
        yield from ("{name}: {type} = None".format(**param) for param in self.parameters if param["is_optional"])

    def request_params_generator(self):
        """
        request_params["chat_id"] = chat_id
        request_params["message_id"] = message_id
        ...
        response = requests.get(url, ..., params=request_params)
        """
        yield f"request_params = {'{}' if (len(self.parameters)) else 'None'}"
        for param in self.parameters:
            line = "request_params['{name}'] = "               # dict that will contain all request parameters
            if any(map(str.isupper, param["type"])):           # args that need to be converted to json are capitalized
                if param["type"].startswith("list["):
                    line += "[item.json for item in {name}]"   # msgs: list[Message] -> [item.json for item in msgs]
                else:
                    line += "{name}.json"                      # msg: Message -> msg.json
            else:
                line += "{name}"
            yield line.format(**param)

    def pythonify_return_type(self):
        """Replaces return type with its python version"""
        for old, new in self.replacements.items():
            if old in self.return_type:
                self.return_type = self.return_type.replace(old, new)

    def pythonify_return_statement(self):
        """return list[str] -> return [str(item) for item in result]"""
        if self.return_type.startswith("list["):
            return f"[{self.return_type[5:-1]}(item) for item in result]"
        return f"{self.return_type}(result)"

    def write_to_file(self, path):
        with open(path, "a", encoding="utf-8") as output_file:
            output_file.write(self.template.format(name=self.name,
                                                   params=", ".join(self.parameter_generator()),
                                                   return_type=self.return_type,
                                                   description="\n    ".join(self.docstring_generator("param")),
                                                   request_params=f"\n    ".join(self.request_params_generator()),
                                                   return_statement=self.pythonify_return_statement()))
            output_file.write("\n\n\n")
