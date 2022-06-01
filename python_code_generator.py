from keyword import iskeyword
from base_code_generator import *


class PythonObjectWriter(BaseObject):
    template_path = "Templates/Python/type_template.txt"
    replacements = {
        " or ": " | ",
        "[": "list[",
        "Boolean": "bool",
        "Integer": "int",
        "Int": "int",
        "Float": "float",
        "String": "str"}
    header = "# This code in its entirety was generated and formated automatically\n\n"

    with open(template_path, "r", encoding="unicode_escape") as template_file:
        template = template_file.read()

    def __init__(self, name, description, parameters):
        super().__init__(name, description, parameters)
        self.pythonify_parameters()

    def pythonify_parameters(self):
        for i, parameter in enumerate(self.parameters):
            if iskeyword(parameter["name"]):
                self.parameters[i]["name"] += "_"
            for old, new in PythonObjectWriter.replacements.items():
                self.parameters[i]["type"] = self.parameters[i]["type"].replace(old, new)

    def get_argument_list(self):
        return ["{name}: {type}".format(**param) for param in self.parameters if not param["is_optional"]] + \
               ["{name}: {type} = None".format(**param) for param in self.parameters if param["is_optional"]]

    @classmethod
    def write_file_header(cls, path):
        with open(path, "w", encoding="utf-8") as output_file:
            output_file.write(cls.header)

    def write_to_file(self, path):
        with open(path, "a", encoding="utf-8") as output_file:
            output_file.write(self.template.format(name=self.name, description=self.description))
            output_file.write("\n\n")


class PythonMethodWriter(PythonObjectWriter, BaseMethod):
    template_path = "Templates/Python/method_template.txt"
    header = PythonObjectWriter.header + ("import requests\n"
                                          "from types import *\n\n"
                                          f"API_URL = '{API_URL}'\n"
                                          "token = 'your_bot_token_here'\n"
                                          "\n\n")

    with open(template_path, "r", encoding="unicode_escape") as template_file:
        template = template_file.read()

    def __init__(self, name, description, parameters):
        super().__init__(name, description, parameters)
        self.payload = "\n\t".join(self.payload_generator())
        self.pythonify_return_type()

    def pythonify_return_type(self):
        for old, new in self.replacements.items():
            self.return_type = self.return_type.replace(old, new)

    def payload_generator(self):
        for parameter in self.parameters:
            if parameter["is_optional"]:
                yield "if {name} is not None:\n\t\tpayload['{name}'] = {name}".format(**parameter)
            else:
                yield "payload['{name}'] = {name}".format(**parameter)

    def write_to_file(self, path):
        with open(path, "a", encoding="utf-8") as output_file:
            output_file.write(self.template.format(name=self.name, params=", ".join(self.get_argument_list()),
                                                   return_type=self.return_type, description=self.description,
                                                   payload=self.payload))
            output_file.write("\n\n")