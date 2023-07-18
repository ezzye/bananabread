import json

# claude second try

# Page structure JSON
with open('page_structure.json') as f:
    page_structure = json.load(f)

# Data units JSON  
with open('data_units.json') as f:
    data_units = json.load(f)

# Find common parent attributes
def find_common_parents(struct, tag, attr_key):
    common = []
    stack = []
    for item in struct:
        if item['tag'] == tag:
            for key, values in item['attributes'].items():
                if key == attr_key:
                    stack.extend(values)
        elif 'children' in item:
            stack.append(item['tag'])
            common = find_common_parents(item['children'], tag, attr_key)
            stack.pop()

    return common

# Extract attributes
results = {
    'attributes': {
        'data unit item including title link text': find_common_parents(page_structure, 'body', 'class'),
        'title': find_common_parents(page_structure, 'h3', 'class'),
        'link': find_common_parents(page_structure, 'a', 'class'),
        'text': find_common_parents(page_structure, 'span', 'class')
    }
}

print(json.dumps(results, indent=2))