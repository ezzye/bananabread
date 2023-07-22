#!/usr/bin/env python

import json

# gpt-4-code-interpreter -- does not seem to find attributes for "data unit item including title link text" but looks
# promising.  Got to work with a few changes so was on right track

# Define the stack for storing attributes
attributes_stack = []
success = 0

# Define a dictionary for storing the common parent attributes
common_parent_attributes = {
    "data_unit": [],
    "title": [],
    "link": [],
    "text": []
}


# Define the function for DFS
def dfs(node):
    # Push the node's attributes into the stack
    global success
    if "class" in node["attributes"]:
        attributes_stack.append(node["attributes"]["class"])

    # Check if the node's text or link is in the data units
    for unit in data_units:
        if node["text"]:
            if unit['text'] in node["text"] and node["tag"] != "h3":
                common_parent_attributes["text"].append(attributes_stack[-1:])
                success += 1
        if node["link"]:
            if unit['link'] in node["link"]:
                common_parent_attributes["link"].append(attributes_stack[-1:])
                success += 1
        if node["text"]:
            if unit['title'] in node["text"] and node["tag"] == "h3":
                common_parent_attributes["title"].append(attributes_stack[-1:])
                success += 1

    # Visit the children of the node
    for child in node["children"]:
        dfs(child)

    # Pop the node's attributes from the stack
    if "class" in node["attributes"]:
        # for _ in node["attributes"]["class"]:
        attributes_stack.pop()
        if success == 3:
            common_parent_attributes["data_unit"].append(attributes_stack[-3])
            success = 0


def load_file(json_file_path):
    # Load the JSON data
    with open(json_file_path, 'r') as f:
        data = json.load(f)
    return data


def save_file(data, json_file_path):
    # Save the JSON data
    with open(json_file_path, 'w') as f:
        json.dump(data, f, indent=2)


# Load the data units
data_units = load_file("banana/data_unit.json")

# Convert the data_units into a set for efficient search
data_units_set_title = set()
data_units_set_link = set()
data_units_set_text = set()
for data_unit in data_units:
    data_units_set_title.add(data_unit["title"])
    data_units_set_link.add(data_unit["link"])
    data_units_set_text.add(data_unit["text"])

# Load the page structure
page_structure = load_file("banana/webpage_content.json")

# Start the DFS
dfs(page_structure)

save_file(common_parent_attributes, "banana/common_parent_attributes.json")
