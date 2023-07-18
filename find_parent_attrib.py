import json

# Open ai gpt-3.5-turbo-16k-0613

def find_common_parents(page_structure, units_data):
    common_parent_attrs = {
        "attributes": {
            "data unit item including title link text": [],
            "title": [],
            "link": [],
            "text": []
        }
    }
    stack = []

    def iterate_page_structure(structure):
        nonlocal stack
        tag = structure.get("tag")
        attributes = structure.get("attributes", {})
        text = structure.get("text")
        link = structure.get("link")

        if tag == "a":
            stack.append(attributes.get("class", []))
            if text:
                stack.append(attributes.get("class", []))
                common_parent_attrs["attributes"]["link"] = stack.copy()
                stack.pop()
        elif text:
            stack.append(attributes.get("class", []))
            common_parent_attrs["attributes"]["text"] = stack.copy()
            stack.pop()

        if tag in ["h1", "h2", "h3", "h4", "h5", "h6"]:
            title = text if text else ""
            stack.append(attributes.get("class", []))
            common_parent_attrs["attributes"]["title"] = stack.copy()
            stack.pop()

        stack.append(attributes.get("class", []))

        for child_structure in structure.get("children", []):
            iterate_page_structure(child_structure)

        stack.pop()

    for unit_data in units_data:
        stack = []
        iterate_page_structure(page_structure)
        common_parent_attrs["attributes"]["data unit item including title link text"] = stack.copy()

    return common_parent_attrs


if __name__ == "__main__":
    with open("page_structure.json", "r") as file:
        page_structure = json.load(file)

    with open("units_data.json", "r") as file:
        units_data = json.load(file)

    common_parent_attributes = find_common_parents(page_structure, units_data)

    with open("output.json", "w") as file:
        json.dump(common_parent_attributes, file)
