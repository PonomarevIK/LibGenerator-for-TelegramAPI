import bs4
import os
from writers import PythonObjectWriter, PythonMethodWriter

DOCS_LOCATION = "https://core.telegram.org/bots/api"


@property
def next_sibling_tag(self):
    tag = self
    while tag is not None:
        tag = tag.next_sibling
        if type(tag) == bs4.element.Tag:
            return tag
    return None
bs4.element.PageElement.next_sibling_tag = next_sibling_tag



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
    methods_output_file.write(PythonMethodWriter.header)

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

        if name[0].islower():
            # To distinguish a section containing method description from any other section we look for an <h4> header
            # that starts with a lowercase letter. Other ways (like having a word "method" in section's description)
            # are not consistent across the entire documentation
            tg_method = PythonMethodWriter(name, description, parameters)
            methods_output_file.write(method_template.format(name=tg_method.name,
                                                             params=", ".join(tg_method.get_argument_list()),
                                                             return_type=tg_method.return_type,
                                                             description=tg_method.description,
                                                             payload=tg_method.payload))
            methods_output_file.write("\n\n")
        elif " " not in name:
            tg_object = PythonObjectWriter(name, description, parameters)
            types_output_file.write(type_template.format(name=tg_object.name, description=tg_object.description))
            types_output_file.write("\n\n")
            # pass

    types_output_file.close()
    methods_output_file.close()

    # os.system('autopep8 --in-place --aggressive --aggressive "Generated code/Python/methods.py"')


if __name__ == "__main__":
    main()
