import json


# open ai gpt-4 default

def add_attributes_to_stack(node, stack):
    stack.append(node["attributes"])


def remove_attributes_from_stack(stack):
    stack.pop()


def find_attributes(node, stack, title, link, text):
    if node["tag"] == "a":
        if node["text"] == link:
            return stack[-1]
        elif node["text"] == title:
            return stack[-1]
    elif node["text"] == text:
        return stack[-1]
    return None


def recursive_search(node, stack, title, link, text):
    add_attributes_to_stack(node, stack)

    attr = find_attributes(node, stack, title, link, text)
    if attr is not None:
        return attr

    for child in node["children"]:
        attr = recursive_search(child, stack, title, link, text)
        if attr is not None:
            return attr

    remove_attributes_from_stack(stack)
    return None


def parse_page_structure(json_structure, data_units):
    page_structure = json.loads(json_structure)
    output = {"attributes": {}}

    for data_unit in data_units:
        title = data_unit["title"]
        link = data_unit["link"]
        text = data_unit["text"]
        stack = []

        output["attributes"]["data unit item including title link text"] = recursive_search(page_structure, stack,
                                                                                            title, link, text)
        output["attributes"]["title"] = recursive_search(page_structure, stack, title, link, text)
        output["attributes"]["link"] = recursive_search(page_structure, stack, title, link, text)
        output["attributes"]["text"] = recursive_search(page_structure, stack, title, link, text)

    with open('output.json', 'w') as json_file:
        json.dump(output, json_file)


# Load JSON structures
with open('page_structure.json') as json_file:
    json_structure = json_file.read()

with open('data_units.json') as json_file:
    data_units = json.load(json_file)

# Parse page structure
parse_page_structure(json_structure, data_units)
