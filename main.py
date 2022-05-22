import bs4
from keyword import iskeyword

# either a url to get API documentation from, or path to locally stored documentation HTML file
DOCS_LOCATION = "https://core.telegram.org/bots/api"
# DOCS_LOCATION = "Telegram Bot API.html"
API_URL = "https://api.telegram.org/bot{token}/{method}"  # url to send API requests


@property
def next_sibling_tag(self):
    tag = self
    while tag is not None:
        tag = tag.next_sibling
        if type(tag) == bs4.element.Tag:
            return tag
    return None
bs4.element.PageElement.next_sibling_tag = next_sibling_tag


class BaseTgType:
    def __init__(self, name, description, parameters):
        self.name = name
        self.description = description
        self.parameters = parameters


class BaseTgMethod(BaseTgType):
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


class PythonTgType(BaseTgType):
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
        # return ["{name}: {type}{default}".format(**parameter, default=" = None" if parameter["is_optional"] else "")
        #         for parameter in self.parameters]

    def __str__(self):
        return f"class {self.name}:\n    def __init__(self{(', ' if self.parameters else '') + ', '.join(self.get_argument_list())})\n        pass"


class PythonTgMethod(PythonTgType, BaseTgMethod):
    header_lines = ["import requests",
                    "from types import *",
                    "\ntoken = ''",
                    f"API_URL = '{API_URL}'"]
    header = "\n".join(header_lines) + "\n\n"

    def __init__(self, name, description, parameters):
        super().__init__(name, description, parameters)
        self.payload = "\n    ".join(self.payload_generator())
        self.pythonify_return_type()

    def pythonify_return_type(self):
        for old, new in self.replacements.items():
            self.return_type = self.return_type.replace(old, new)

    def payload_generator(self):
        # payload_code = []
        for parameter in self.parameters:
            if parameter["is_optional"]:
                # payload_code.append("if {name} is not None:\n    payload['{name}'] = {name}".format(**parameter))
                yield "if {name} is not None:\n        payload['{name}'] = {name}".format(**parameter)
            else:
                # payload_code.append("payload['{name}'] = {name}".format(**parameter))
                yield "payload['{name}'] = {name}".format(**parameter)
        # return payload_code


    def __str__(self):
        return f"def {self.name}({', '.join(self.get_argument_list())}) -> {self.return_type}:\n    \"\"\"{self.description}\"\"\""


def get_html_tree(source: str, strainer: bs4.SoupStrainer = None, parser="html.parser") -> bs4.BeautifulSoup:
    """Creates a BeautifulSoup object from given HTML file or URL"""
    if source.startswith(("http://", "https://")):
        import requests
        return bs4.BeautifulSoup(requests.get(source).text, parser, parse_only=strainer)
    with open(source) as html_file:
        return bs4.BeautifulSoup(html_file, parser, parse_only=strainer)


def parse_table(table: bs4.element.Tag):
    """Parses an HTML <table> and returns a list of data from each row of the table's body"""
    if not isinstance(table, bs4.element.Tag) or table.name != "table":
        raise ValueError("'table' argument must be a BeautifulSoup <table>")

    def format_types(types: str):
        types = types.replace("Float number", "Float")  # fixes inconsistent float type naming
        types = types.replace("Array of ", "[") + "]" * types.count("Array of ")  # Array of Array of X -> [[X]]
        types = types.replace(", ", " or ").replace(" and ", " or ")  # Array of X, Y and Z -> [X or Y or Z]
        return types

    parameters = []
    for row in table.tbody.find_all("tr"):
        row_data = [item.text for item in row.find_all("td")]
        parameter = {"name": row_data[0],
                     "type": format_types(row_data[1]),
                     "is_optional": row_data[2].startswith("Optional"),
                     "description": row_data[-1].removeprefix("Optional. ")}
        parameters.append(parameter)
    return parameters


def main(language="Python"):
    # html tree within div#dev_page_content - div containing everything we need to parse
    soup = get_html_tree(DOCS_LOCATION, bs4.SoupStrainer("div", id="dev_page_content"))
    # this is where introduction ends and objects/methods documentation begins, <h3>...Getting updates</h3>
    docs_beginning = soup.find("a", class_="anchor", href="#getting-updates")

    types_output_file = open(f"Generated code\\{language}\\types.py", "w")

    methods_output_file = open(f"Generated code\\{language}\\methods.py", "w", encoding="utf-8")
    methods_output_file.write(PythonTgMethod.header)

    with open(f"Templates\\{language}\\type_template.txt", "r") as t_template:
        type_template = t_template.read()
    with open(f"Templates\\{language}\\method_template.txt", "r") as m_template:
        method_template = m_template.read()

    for h4 in docs_beginning.find_all_next("h4"):
        name = h4.text

        paragraph = h4.next_sibling_tag
        description = paragraph.text if paragraph.name == "p" else ""

        table = paragraph.next_sibling_tag
        parameters = parse_table(table) if table.name == "table" else []

        if h4.text[0].islower():
            # To distinguish a section containing method description from any other section we look for an <h4> header
            # that starts with a lowercase letter. Other ways (like having a word "method" in section's description)
            # are not consistent across the entire documentation
            tg_method = PythonTgMethod(name, description, parameters)
            methods_output_file.write(method_template.format(name=tg_method.name,
                                                             params=", ".join(tg_method.get_argument_list()),
                                                             return_type=tg_method.return_type,
                                                             description=tg_method.description,
                                                             payload=tg_method.payload))
            methods_output_file.write("\n\n")
            # pass
        else:
            if " " in name:
                continue
            tg_object = PythonTgType(name, description, parameters)
            types_output_file.write(type_template.format(name=tg_object.name, description=tg_object.description))
            types_output_file.write("\n\n")
            # pass

    types_output_file.close()
    methods_output_file.close()


if __name__ == "__main__":
    main()