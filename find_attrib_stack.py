import json

# gpt-4-code interpreter

# Define the stack for storing attributes
attributes_stack = []

# Define a dictionary for storing the common parent attributes
common_parent_attributes = {
    "data unit item including title link text": [],
    "title": [],
    "link": [],
    "text": []
}

# Define the data units for search
data_units = [
    {
        "title": "Marc Bolan's London House in Hackney: The Early Years",
        "link": "https://www.hangerlondon.com/marc-bolan-london/",
        "text": "Marc Bolan, born Mark Feld on 30/9/1947 grew up in London's Stoke Newington and lived in this house at 25 Stoke Newington Common."
    }
]

# Convert the data_units into a set for efficient search
data_units_set = set()
for data_unit in data_units:
    data_units_set.add(data_unit["title"])
    data_units_set.add(data_unit["link"])
    data_units_set.add(data_unit["text"])

# Define the function for DFS
def dfs(node):
    # Push the node's attributes into the stack
    if "class" in node["attributes"]:
        attributes_stack.extend(node["attributes"]["class"])

    # Check if the node's text or link is in the data units
    if node["text"] in data_units_set:
        common_parent_attributes["text"].extend(attributes_stack[-1:])
        data_units_set.remove(node["text"])
    if node["link"] in data_units_set:
        common_parent_attributes["link"].extend(attributes_stack[-1:])
        data_units_set.remove(node["link"])

    # Visit the children of the node
    for child in node["children"]:
        dfs(child)

    # Pop the node's attributes from the stack
    if "class" in node["attributes"]:
        for _ in node["attributes"]["class"]:
            attributes_stack.pop()

# Load the page structure
page_structure = json.loads(page_structure_json_str)

# Start the DFS
dfs(page_structure)

# Print the common parent attributes
print(json.dumps(common_parent_attributes, indent=2))
