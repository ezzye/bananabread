# LLM Iteration Pattern


## Introduction
Code performs an action based on one of a list of assumption and a set of inputs.
Code then checks if output matches a description which includes examples using a LLM.
If the output does not match the description then the code changes the assumption and repeats the process.
The code makes a change to the assumption using a function that takes the output of LLM and outputting next assumption.

## Example
Imagine a python script that takes a html webpage web_response object from 
```python
session = HTMLSession()
web_response = session.get(url, headers=headers)
session.close()
```
Assumption is that the webpage contains structured repeating data that can be extracted using a css selector (css identifier).
However, the identity of the css selector for the repeating units of data is unknown.

A function is created that takes the web_response object and outputs a list of css selectors based on an example of repeating text such as
titles for each unit that have common containing css identifiers.  The list is ordered by distance from example text.

There is also a scrape function that takes examples of data in each unit of data in web page together with a description of item.
The scrape function then takes nearest common css identifier for each item and attempts to scape data by iterating 
through each assumed unit of data and using the css identifier to extract data.
```python
def parse_results(response: object, 
                  test_unit_data_css_id,
                  test_css_identifier_title,
                  test_css_identifier_link,
                  test_css_identifier_text) -> object:
    assumed_css_identifier_for_unit_data = test_unit_data_css_id
    css_identifier_title = test_css_identifier_title
    css_identifier_link = test_css_identifier_link
    css_identifier_text = test_css_identifier_text

    results = response.html.find(assumed_css_identifier_for_unit_data)

    output = []

    for result in results:
        title = result.find(css_identifier_title, first=True)
        link = result.find(css_identifier_link, first=True)
        test = result.find(css_identifier_text, first=True)
        if title is None or link is None or test is None:
            continue
        item = {
            'title': title.text,
            'link': link.attrs['href'],
            'text': test.text
        }

        output.append(item)

    return output
```
The output of the scrape function is then compared to the description of the output for a particular 
assumed unit of data css identifier in LLM assumption function.

If output matches description then rest of webpages scaped using the same assumption.

If output does not match description then depending on scraped output sraping function is called again with altered 
css identifier for unit of data from list and/or different individual data css identifiers based on python decision function.

An example decision function would take the following into account
- how many units of data were scraped.  This is most important
- Was only items scraped without additional tags
- if no data items were scraped then was there a common css identifier for units of data

So the functions needed are:
- LLM test assumption function
- Choose CSS  identifier function
- Webpage scrape function (/)