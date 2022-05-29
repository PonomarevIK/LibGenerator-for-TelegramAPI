import bs4
import requests
import os

import writers


DOCS_LOCATION = "https://core.telegram.org/bots/api"


def next_sibling_tag(tag):
    while tag is not None:
        tag = tag.next_sibling
        if type(tag) == bs4.element.Tag:
            return tag
    return None


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


def main(language):
    soup = bs4.BeautifulSoup(requests.get(DOCS_LOCATION).text, "html.parser", parse_only=bs4.SoupStrainer("div", id="dev_page_content"))

    for h4 in soup.find_all("h4"):
        name = h4.text

        paragraph = next_sibling_tag(h4)
        description = paragraph.text if paragraph.name == "p" else ""

        table = next_sibling_tag(paragraph)
        parameters = parse_table(table) if table.name == "table" else []

        if name[0].islower():
            # To distinguish a section containing method description from any other section
            # look for an <h4> header that starts with a lowercase letter
            tg_method = writers.PythonMethodWriter(name, description, parameters)
            tg_method.write_to_file()
        elif " " not in name:
            tg_object = writers.PythonObjectWriter(name, description, parameters)
            tg_object.write_to_file()

    os.system('autopep8 --in-place --aggressive "Generated code/Python/methods.py"')
    # os.system('autopep8 --in-place --aggressive "Generated code/Python/types.py"')


if __name__ == "__main__":
    main("Python")
