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
        self.request_params = "\n    ".join(self.request_params_generator())
        self.pythonify_return_type()

    def argument_generator(self):
        yield from ("{name}: {type}".format(**arg) for arg in self.parameters if not arg["is_optional"])
        yield from ("{name}: {type} = None".format(**arg) for arg in self.parameters if arg["is_optional"])

    def request_params_generator(self):
        # todo: result = "reqest_params['{name}']" + ...
        yield f"request_params = {'{}' if len(self.parameters) else 'None'}"
        for param in self.parameters:
            if param["type"].startswith("list["):
                yield "reqest_params['{name}'] = [item for item in {name}]".format(**param)
            elif any(map(str.isupper, param["type"])):
                yield "request_params['{name}'] = {name}.json".format(**param)
            else:
                yield "request_params['{name}'] = {name}".format(**param)
        # [item.json for item in caption_entities] if startswith list[]

    def pythonify_return_type(self):
        for old, new in self.replacements.items():
            self.return_type = self.return_type.replace(old, new)

    def pythonify_return_statement(self):
        if self.return_type.startswith("list["):
            return f"{self.return_type[5:-1]}(item) for item in "
        return ""

    def write_to_file(self, path):
        with open(path, "a", encoding="utf-8") as output_file:
            output_file.write(self.template.format(name=self.name, args=", ".join(self.argument_generator()),
                                                   return_type=self.return_type, description=self.description,
                                                   request_params="\n    ".join(self.request_params_generator()),
                                                   return_statement=self.pythonify_return_statement()))
            output_file.write("\n\n\n")
