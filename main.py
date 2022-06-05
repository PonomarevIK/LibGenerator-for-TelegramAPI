import bs4
import requests
import os

DOCS_LOCATION = "https://core.telegram.org/bots/api"


def next_sibling_tag(tag):
    while tag is not None:
        tag = tag.next_sibling
        if type(tag) == bs4.element.Tag:
            return tag
    return None


def format_types(types: str):
    types = types.replace("Float number", "Float")  # fixes inconsistent float type naming
    types = types.replace("Array of ", "[") + "]" * types.count("Array of ")  # Array of Array of X -> [[X]]
    types = types.replace(", ", " or ").replace(" and ", " or ")  # Array of X, Y and Z -> [X or Y or Z]
    return types


def parse_table(table: bs4.element.Tag):
    """Parses an HTML <table> and returns a list of data from each row"""
    if not isinstance(table, bs4.element.Tag) or table.name != "table":
        raise ValueError("'table' argument must be a BeautifulSoup <table>")

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
    soup = bs4.BeautifulSoup(requests.get(DOCS_LOCATION).text, "html.parser",
                             parse_only=bs4.SoupStrainer("div", id="dev_page_content"))

    if language.lower() == "python":
        import python_code_generator
        method_writer = python_code_generator.PythonMethodWriter
        object_writer = python_code_generator.PythonObjectWriter
    else:
        raise NotImplementedError(f"{language} is not implemented yet")

    method_output_file = f"Generated code/{language}/methods.py"
    object_output_file = f"Generated code/{language}/types.py"

    method_writer.write_file_header(method_output_file)
    object_writer.write_file_header(object_output_file)

    for h4 in soup.find_all("h4"):
        name = h4.text

        if " " in name:
            continue  # headers that contain spaces are skipped, they are neither methods nor objects

        paragraph = next_sibling_tag(h4)
        description = paragraph.text if paragraph.name == "p" else ""

        table = next_sibling_tag(paragraph)
        parameters = parse_table(table) if table.name == "table" else []

        if name[0].islower():
            # Header of section containing method description start with a lowercase letter
            method_writer(name, description, parameters).write_to_file(method_output_file)
        else:
            # Header of section containing object description start with an uppercase letter
            object_writer(name, description, parameters).write_to_file(object_output_file)

    # Code file formatting and beautifying
    if language == "Python":
        os.system(f'autopep8 --in-place --aggressive --aggressive "{method_output_file}"')
        os.system(f'autopep8 --in-place --aggressive --aggressive "{object_output_file}"')


if __name__ == "__main__":
    main("Python")
