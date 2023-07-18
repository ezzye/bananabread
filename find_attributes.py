import json

# first try with claude

# Input JSON data
page_structure_json = ""  # JSON data for page structure
text_examples_json = ""  # JSON data for text examples

# Extract common tags and attributes from page structure
common_tags = {}
common_attributes = {}
for item in page_structure_json:
    for child in item['children']:
        tag = child['tag']
        if tag not in common_tags:
            common_tags[tag] = 0
        common_tags[tag] += 1

        for key, value in child['attributes'].items():
            if key not in common_attributes:
                common_attributes[key] = {}
            for attr in value:
                if attr not in common_attributes[key]:
                    common_attributes[key][attr] = 0
                common_attributes[key][attr] += 1

# Extract attributes from text examples
text_attributes = {
    'title': [],
    'link': [],
    'text': []
}

for item in text_examples_json:
    title = item['title']
    link = item['link']
    text = item['text']

    title_tag = page_structure_json[0]['children'][0]['children'][1]
    text_attributes['title'].extend(title_tag['attributes']['class'])

    link_tag = page_structure_json[0]['children'][1]['children'][0]['children'][0]
    text_attributes['link'].extend(link_tag['attributes']['class'])

    text_tag = page_structure_json[0]['children'][1]['children'][1]['children'][0]
    text_attributes['text'].extend(text_tag['attributes']['class'])

# Find common attributes
common_values = []
for key, value in common_attributes.items():
    sorted_values = sorted(value.items(), key=lambda x: x[1], reverse=True)
    common_values.append(sorted_values[0][0])

print({
    "attributes": {
        "common values for each data item": common_values,
        "title": text_attributes['title'],
        "link": text_attributes['link'],
        "text": text_attributes['text']
    }
})
