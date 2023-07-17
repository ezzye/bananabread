#!/usr/bin/env python

from requests_html import HTMLSession
import json
import requests
from lxml import etree


def get_request(url, session=None):
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
    }
    web_response = None  # Initialize web_response to None
    if session is None:
        print("You need to pass a session object to this function.")
        exit()

    try:
        web_response = session.get(url, headers=headers)
        session.close()

    except requests.exceptions.RequestException as e:
        print(e)
    return web_response


def get_element_dict(element, visited=None):
    # Initialize the set of visited elements
    if visited is None:
        visited = set()

    # If we've already visited this element, return None
    if element in visited:
        return None

    # Mark this element as visited
    visited.add(element)

    # Ignore the tags such as `script`, `html` and `head`
    if element.tag in ['script', 'html', 'head', 'style', 'jsmodel', 'svg', 'path']:
        return None

    # Ignore attribute value that is longer than 10 characters

    if element.attrs:
        attributes = {key: value for key, value in element.attrs.items() if len(value) <= 10}
    else:
        attributes = {}

    if element.tag in ['a', 'p', 'h1', 'h2' ,'h3' , 'h4', 'h5', 'h6', 'strong', 'i', 'em', 'mark', 'small', 'del', 'ins', 'sub', 'sup', 'span']:
        if len(element.text) <= 250:
            seen_text = element.text[:250]
        else:
            seen_text = None
    else:
        seen_text = None

    if element.tag in ['a']:
        element_link = element.absolute_links
    else:
        element_link = None

    # Get the children of the current element
    children_elements = [e for e in element.find('*')
                         if e.element.getparent() is not None and
                         etree.tostring(e.element.getparent()) == etree.tostring(element.element)]

    children_dicts = [get_element_dict(child) for child in children_elements]
    children_dicts = [d for d in children_dicts if d is not None]  # Filter out None values

    element_dict = {
        'tag': element.tag,
        'attributes': attributes,
        'text': seen_text,
        'link': str(element_link),
        'children': children_dicts
    }

    return element_dict


def get_webpage_content(url, session=None):
    if session is None:
        session = HTMLSession()

    web_response = get_request(url, session=session)

    root_element = web_response.html.find('body', first=True)

    webpage_dict = get_element_dict(root_element)

    return webpage_dict


# Main script
if __name__ == '__main__':
    url = "https://www.google.com/search?q=Marc+Bolan+Stoke+Newington&start=0&sourceid=chrome&ie=UTF-8"
    webpage_dict = get_webpage_content(url)

    # Save the webpage_dict as a JSON file

    with open('webpage_content.json', 'w') as json_file:
        json.dump(webpage_dict, json_file, indent=4)

    print("The content of the webpage has been saved to 'webpage_content.json'.")
