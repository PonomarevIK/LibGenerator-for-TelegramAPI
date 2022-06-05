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
        "String": "str"}
    header = "# This code in its entirety was generated and formatted automatically\n\n"

    with open(template_path, "r", encoding="unicode_escape") as template_file:
        template = template_file.read()

    def __init__(self, name, description, parameters):
        super().__init__(name, description, parameters)
        self.pythonify_parameters()

    def pythonify_parameters(self):
        for i, parameter in enumerate(self.parameters):
            if iskeyword(parameter["name"]):
                self.parameters[i]["name"] += "_"
            for old, new in self.replacements.items():
                self.parameters[i]["type"] = self.parameters[i]["type"].replace(old, new)

    def init_generator(self):
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
            yield line.format(**attr)

    @classmethod
    def write_file_header(cls, path):
        with open(path, "w", encoding="utf-8") as output_file:
            output_file.write(cls.header)

    def write_to_file(self, path):
        with open(path, "a", encoding="utf-8") as output_file:
            output_file.write(self.template.format(name=self.name,
                                                   description=self.description,
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
        yield from ("{name}: {type}".format(**param) for param in self.parameters if not param["is_optional"])
        yield from ("{name}: {type} = None".format(**param) for param in self.parameters if param["is_optional"])

    def docstring_generator(self):
        yield self.description
        yield from (":param {name}: {description}".format(**param) for param in self.parameters)

    def request_params_generator(self):
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
        for old, new in self.replacements.items():
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
                                                   description="\n    ".join(self.docstring_generator()),
                                                   request_params=f"\n    ".join(self.request_params_generator()),
                                                   return_statement=self.pythonify_return_statement()))
            output_file.write("\n\n\n")
