import json


# Bard
def find_common_parent_attributes(page_structure):
    """Finds common parent attribute values for individual text and link examples that form part of a unit of data.

    Args:
      page_structure: The page structure JSON file.

    Returns:
      A dictionary of common parent attribute values for title, link and text and units of data.
    """

    common_parent_attributes = {}
    stack = []

    for node in page_structure:
        if node["tag"] == "a":
            common_parent_attributes["link"] = node["attributes"]
        elif node["text"] is not None:
            common_parent_attributes["text"] = node["attributes"]
        else:
            for attribute in node["attributes"]:
                if attribute not in stack:
                    stack.append(attribute)
            common_parent_attributes["unit_of_data"] = stack
            stack = []

    return common_parent_attributes


if __name__ == "__main__":
    with open("page_structure.json") as f:
        page_structure = json.load(f)

    common_parent_attributes = find_common_parent_attributes(page_structure)

    print(common_parent_attributes)
