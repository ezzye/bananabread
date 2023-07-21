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

### Python script to test results of a scrape matches example and output analysis
If the scrape has correctly worked then it would have extracted information from a list of units of data.
If not then items will:
- repeat
- be missing
- contain too much information
- contain too little information
- be in the wrong order
- be in the wrong format
- to few units of data
- too many units of data

The python script will then analyse the output of the scrape function and return a list of possible problems.

Input:
SPAN,DIV, P, H, A and tags with attributes and text

### Python script to extract css identifiers from example url
Write a python script that takes a url and outputs a dictionary (as a json file) of `body`, `span`, `div`, `p`, `h` and  `a` and tags with attributes and text
that represents the page.
The dictionary should be structured to represent the structure of the page.
Ignore other tags such as `script`, `html` and `head` etc
Also ignore attribute value that is longer than 10 characters.
Use 
```python
session = HTMLSession()
web_response = session.get(url, headers=headers)
session.close()
```
and extract elements and add to dictionary.
```python
all_elements = web_response.html.find('*')
```
and for each element in all_elements extract the tag and attributes and text and add to dictionary.
```python
each_element = all_elements[0]
attributes_for_element = each_element.attrs
text_for_element = each_element.text
```

## Write python script to iterate through page structure json file  and find example texts and links in page structure and suggest css identifiers for each item and common to data units
Write python script to find common parent attribute values for individual text and link examples that form part of a unit of data. It should also
find common parent attribute values for units of data.

It should do this br using a stack and recursively iterating through the page structure json file adding attribute values to the stack when new children are found
and removing attribute values from the stack when children are finished until has found all examples of text and links and units of data.  
The top of the stack just before a unit of data is finished is the common parent attribute values for the unit of data, text or link example.

Title is not in a "a" anchor tag.
Link is in a "a" anchor tag.
Test is in a tag visible to user.

The script should load the page structure json file and json list of data units file and 
output a json file showing attribute values for title, link and text and units of data.

An example page structure json file:
```json
{
  "tag": "body",
  "attributes": {
    "jsmodel": "hspDDf",
    "class": [
      "srp"
    ],
    "jscontroller": "Eox39d",
    "marginheight": "3",
    "topmargin": "3",
    "id": "gsr"
  },
  "text": null,
  "link": "None",
  "children": [
    {
      "tag": "div",
      "attributes": {},
      "text": null,
      "link": "None",
      "children": []
    },
    {
      "tag": "noscript",
      "attributes": {},
      "text": null,
      "link": "None",
      "children": [
        {
          "tag": "meta",
          "attributes": {
            "http-equiv": "refresh"
          },
          "text": null,
          "link": "None",
          "children": []
        },
        {
          "tag": "div",
          "attributes": {},
          "text": null,
          "link": "None",
          "children": [
            {
              "tag": "a",
              "attributes": {},
              "text": "here",
              "link": "{'https://www.google.com/search?q=Marc+Bolan+Stoke+Newington&gbv=1&sei=S3e1ZIPBNeSjkdUPxIGZiAg'}",
              "children": []
            }
          ]
        }
      ]
    },
    {
      "tag": "h1",
      "attributes": {
        "class": [
          "Uo8X3b",
          "OhScic",
          "zsYMMe"
        ]
      },
      "text": "Accessibility links",
      "link": "None",
      "children": []
    },
    {
      "tag": "div",
      "attributes": {
        "jscontroller": "EufiNb",
        "class": [
          "wYq63b"
        ]
      },
      "text": null,
      "link": "None",
      "children": [
        {
          "tag": "div",
          "attributes": {
            "class": [
              "S6VXfe"
            ]
          },
          "text": null,
          "link": "None",
          "children": [
            {
              "tag": "a",
              "attributes": {
                "jsname": "BKxS1e",
                "class": [
                  "gyPpGe"
                ],
                "role": "link",
                "tabindex": "0",
                "jsaction": "i3viod"
              },
              "text": "Skip to main content",
              "link": "set()",
              "children": []
            },
            {
              "tag": "a",
              "attributes": {
                "jsname": "KI37ad",
                "class": [
                  "gyPpGe"
                ]
              },
              "text": "Accessibility help",
              "link": "{'https://support.google.com/websearch/answer/181196?hl=en-GB'}",
              "children": []
            },
            {
              "tag": "div",
              "attributes": {},
              "text": null,
              "link": "None",
              "children": [
                {
                  "tag": "div",
                  "attributes": {
                    "jscontroller": "EkevXb"
                  },
                  "text": null,
                  "link": "None",
                  "children": []
                },
                {
                  "tag": "div",
                  "attributes": {
                    "id": "duf3-78",
                    "data-jiis": "up",
                    "data-async-type": "duffy3",
                    "class": [
                      "yp"
                    ]
                  },
                  "text": null,
                  "link": "None",
                  "children": [{
                    "tag": "div",
                    "attributes": {
                      "class": [
                        "eqAnXb"
                      ],
                      "id": "res",
                      "role": "main"
                    },
                    "text": null,
                    "link": "None",
                    "children": [
                      {
                        "tag": "div",
                        "attributes": {
                          "jscontroller": "SC7lYd",
                          "class": [
                            "g",
                            "Ww4FFb",
                            "vt6azd",
                            "tF2Cxc",
                            "asEBEc"
                          ],
                          "lang": "en",
                          "data-hveid": "CBAQAA"
                        },
                        "text": null,
                        "link": "None",
                        "children": [
                          {
                            "tag": "div",
                            "attributes": {
                              "class": [
                                "kvH3mc",
                                "BToiNc",
                                "UK95Uc"
                              ]
                            },
                            "text": null,
                            "link": "None",
                            "children": [
                              {
                                "tag": "div",
                                "attributes": {
                                  "class": [
                                    "Z26q7c",
                                    "UK95Uc",
                                    "jGGQ5e"
                                  ],
                                  "data-snf": "x5WNvb",
                                  "data-snhf": "0"
                                },
                                "text": null,
                                "link": "None",
                                "children": [
                                  {
                                    "tag": "div",
                                    "attributes": {
                                      "class": [
                                        "yuRUbf"
                                      ]
                                    },
                                    "text": null,
                                    "link": "None",
                                    "children": [
                                      {
                                        "tag": "a",
                                        "attributes": {
                                          "jsname": "ACyKwe"
                                        },
                                        "text": "Marc Bolan's London House in Hackney: The Early Years\nhangerlondon.com\nhttps://www.hangerlondon.com \u203a marc-bolan-london",
                                        "link": "{'https://www.hangerlondon.com/marc-bolan-london/'}",
                                        "children": [
                                          {
                                            "tag": "br",
                                            "attributes": {},
                                            "text": null,
                                            "link": "None",
                                            "children": []
                                          },
                                          {
                                            "tag": "h3",
                                            "attributes": {
                                              "class": [
                                                "LC20lb",
                                                "MBeuO",
                                                "DKV0Md"
                                              ]
                                            },
                                            "text": "Marc Bolan's London House in Hackney: The Early Years",
                                            "link": "None",
                                            "children": []
                                          },
                                          {
                                            "tag": "div",
                                            "attributes": {
                                              "class": [
                                                "TbwUpd",
                                                "NJjxre",
                                                "iUh30",
                                                "apx8Vc",
                                                "ojE3Fb"
                                              ]
                                            },
                                            "text": null,
                                            "link": "None",
                                            "children": [
                                              {
                                                "tag": "span",
                                                "attributes": {
                                                  "class": [
                                                    "H9lube"
                                                  ]
                                                },
                                                "text": "",
                                                "link": "None",
                                                "children": [
                                                  {
                                                    "tag": "div",
                                                    "attributes": {
                                                      "class": [
                                                        "eqA2re",
                                                        "NjwKYd",
                                                        "Vwoesf"
                                                      ],
                                                      "aria-hidden": "true"
                                                    },
                                                    "text": null,
                                                    "link": "None",
                                                    "children": [
                                                      {
                                                        "tag": "img",
                                                        "attributes": {
                                                          "class": [
                                                            "XNo5Ab"
                                                          ],
                                                          "alt": ""
                                                        },
                                                        "text": null,
                                                        "link": "None",
                                                        "children": []
                                                      }
                                                    ]
                                                  }
                                                ]
                                              },
                                              {
                                                "tag": "div",
                                                "attributes": {},
                                                "text": null,
                                                "link": "None",
                                                "children": [
                                                  {
                                                    "tag": "span",
                                                    "attributes": {
                                                      "class": [
                                                        "VuuXrf"
                                                      ]
                                                    },
                                                    "text": "hangerlondon.com",
                                                    "link": "None",
                                                    "children": []
                                                  },
                                                  {
                                                    "tag": "div",
                                                    "attributes": {
                                                      "class": [
                                                        "byrV5b"
                                                      ]
                                                    },
                                                    "text": null,
                                                    "link": "None",
                                                    "children": [
                                                      {
                                                        "tag": "cite",
                                                        "attributes": {
                                                          "class": [
                                                            "apx8Vc",
                                                            "qLRx3b",
                                                            "tjvcx",
                                                            "GvPZzd",
                                                            "cHaqb"
                                                          ],
                                                          "role": "text"
                                                        },
                                                        "text": null,
                                                        "link": "None",
                                                        "children": [
                                                          {
                                                            "tag": "span",
                                                            "attributes": {
                                                              "class": [
                                                                "apx8Vc",
                                                                "dyjrff",
                                                                "ob9lvb"
                                                              ],
                                                              "role": "text"
                                                            },
                                                            "text": "\u203a marc-bolan-london",
                                                            "link": "None",
                                                            "children": []
                                                          }
                                                        ]
                                                      }
                                                    ]
                                                  }
                                                ]
                                              }
                                            ]
                                          }
                                        ]
                                      },
                                      {
                                        "tag": "div",
                                        "attributes": {
                                          "class": [
                                            "B6fmyf",
                                            "byrV5b",
                                            "Mg1HEd"
                                          ]
                                        },
                                        "text": null,
                                        "link": "None",
                                        "children": [
                                          {
                                            "tag": "div",
                                            "attributes": {
                                              "class": [
                                                "TbwUpd",
                                                "iUh30",
                                                "apx8Vc",
                                                "ojE3Fb"
                                              ]
                                            },
                                            "text": null,
                                            "link": "None",
                                            "children": [
                                              {
                                                "tag": "span",
                                                "attributes": {
                                                  "class": [
                                                    "H9lube"
                                                  ]
                                                },
                                                "text": "",
                                                "link": "None",
                                                "children": [
                                                  {
                                                    "tag": "div",
                                                    "attributes": {
                                                      "class": [
                                                        "eqA2re",
                                                        "NjwKYd"
                                                      ]
                                                    },
                                                    "text": null,
                                                    "link": "None",
                                                    "children": []
                                                  }
                                                ]
                                              },
                                              {
                                                "tag": "div",
                                                "attributes": {},
                                                "text": null,
                                                "link": "None",
                                                "children": [
                                                  {
                                                    "tag": "span",
                                                    "attributes": {
                                                      "class": [
                                                        "VuuXrf"
                                                      ]
                                                    },
                                                    "text": "hangerlondon.com",
                                                    "link": "None",
                                                    "children": []
                                                  },
                                                  {
                                                    "tag": "div",
                                                    "attributes": {
                                                      "class": [
                                                        "byrV5b"
                                                      ]
                                                    },
                                                    "text": null,
                                                    "link": "None",
                                                    "children": [
                                                      {
                                                        "tag": "cite",
                                                        "attributes": {
                                                          "class": [
                                                            "apx8Vc",
                                                            "qLRx3b",
                                                            "tjvcx",
                                                            "GvPZzd",
                                                            "cHaqb"
                                                          ],
                                                          "role": "text"
                                                        },
                                                        "text": null,
                                                        "link": "None",
                                                        "children": [
                                                          {
                                                            "tag": "span",
                                                            "attributes": {
                                                              "class": [
                                                                "apx8Vc",
                                                                "dyjrff",
                                                                "ob9lvb"
                                                              ],
                                                              "role": "text"
                                                            },
                                                            "text": "\u203a marc-bolan-london",
                                                            "link": "None",
                                                            "children": []
                                                          }
                                                        ]
                                                      },
                                                      {
                                                        "tag": "div",
                                                        "attributes": {
                                                          "class": [
                                                            "eFM0qc",
                                                            "BCF2pd",
                                                            "iUh30"
                                                          ]
                                                        },
                                                        "text": null,
                                                        "link": "None",
                                                        "children": []
                                                      }
                                                    ]
                                                  }
                                                ]
                                              }
                                            ]
                                          },
                                          {
                                            "tag": "div",
                                            "attributes": {
                                              "class": [
                                                "csDOgf",
                                                "BCF2pd",
                                                "L48a4c"
                                              ]
                                            },
                                            "text": null,
                                            "link": "None",
                                            "children": [
                                              {
                                                "tag": "div",
                                                "attributes": {
                                                  "jscontroller": "exgaYe",
                                                  "data-bsextraheight": "0",
                                                  "data-isdesktop": "true"
                                                },
                                                "text": null,
                                                "link": "None",
                                                "children": [
                                                  {
                                                    "tag": "div",
                                                    "attributes": {
                                                      "role": "button",
                                                      "tabindex": "0",
                                                      "jsaction": "RvIhPd",
                                                      "jsname": "I3kE2c",
                                                      "class": [
                                                        "iTPLzd",
                                                        "rNSxBe",
                                                        "lUn2nc"
                                                      ]
                                                    },
                                                    "text": null,
                                                    "link": "None",
                                                    "children": [
                                                      {
                                                        "tag": "span",
                                                        "attributes": {
                                                          "jsname": "czHhOd",
                                                          "class": [
                                                            "D6lY4c",
                                                            "mBswFe"
                                                          ]
                                                        },
                                                        "text": "",
                                                        "link": "None",
                                                        "children": [
                                                          {
                                                            "tag": "span",
                                                            "attributes": {
                                                              "jsname": "Bil8Ae",
                                                              "class": [
                                                                "xTFaxe",
                                                                "z1asCe"
                                                              ]
                                                            },
                                                            "text": "",
                                                            "link": "None",
                                                            "children": []
                                                          }
                                                        ]
                                                      }
                                                    ]
                                                  },
                                                  {
                                                    "tag": "span",
                                                    "attributes": {
                                                      "jsname": "zOVa8"
                                                    },
                                                    "text": "",
                                                    "link": "None",
                                                    "children": []
                                                  }
                                                ]
                                              }
                                            ]
                                          }
                                        ]
                                      }
                                    ]
                                  }
                                ]
                              },
                              {
                                "tag": "div",
                                "attributes": {
                                  "class": [
                                    "Z26q7c",
                                    "UK95Uc"
                                  ],
                                  "data-sncf": "1",
                                  "data-snf": "nke7rc"
                                },
                                "text": null,
                                "link": "None",
                                "children": [
                                  {
                                    "tag": "div",
                                    "attributes": {
                                      "class": [
                                        "VwiC3b",
                                        "yXK7lf",
                                        "MUxGbd",
                                        "yDYNvb",
                                        "lyLwlc",
                                        "lEBKkf"
                                      ]
                                    },
                                    "text": null,
                                    "link": "None",
                                    "children": [
                                      {
                                        "tag": "span",
                                        "attributes": {},
                                        "text": "Marc Bolan, born Mark Feld on 30/9/1947 grew up in London's Stoke Newington and lived in this house at 25 Stoke Newington Common. Stoke Newington was an\u00a0...",
                                        "link": "None",
                                        "children": [
                                          {
                                            "tag": "em",
                                            "attributes": {},
                                            "text": "Marc Bolan",
                                            "link": "None",
                                            "children": []
                                          },
                                          {
                                            "tag": "em",
                                            "attributes": {},
                                            "text": "Stoke Newington",
                                            "link": "None",
                                            "children": []
                                          },
                                          {
                                            "tag": "em",
                                            "attributes": {},
                                            "text": "Stoke Newington",
                                            "link": "None",
                                            "children": []
                                          },
                                          {
                                            "tag": "em",
                                            "attributes": {},
                                            "text": "Stoke Newington",
                                            "link": "None",
                                            "children": []
                                          }
                                        ]
                                      }
                                    ]
                                  }
                                ]
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  }]
                },
                {
                  "tag": "a",
                  "attributes": {
                    "jsname": "JUypV",
                    "class": [
                      "gyPpGe"
                    ],
                    "data-async-trigger": "duf3-78",
                    "role": "link",
                    "tabindex": "0"
                  },
                  "text": "Accessibility feedback",
                  "link": "set()",
                  "children": []
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

Text example input as json list of data units (title, link, text):
```json
[
{
"title": "Marc Bolan's London House in Hackney: The Early Years",
"link": "https://www.hangerlondon.com/marc-bolan-london/",
"text": "Marc Bolan, born Mark Feld on 30/9/1947 grew up in London's Stoke Newington and lived in this house at 25 Stoke Newington Common."
}
]
```
Example output showing attribute values for title, link and text
```json
{
  "attributes": {
    "data unit item including title link text": [
      "g",
      "Ww4FFb",
      "vt6azd",
      "tF2Cxc",
      "asEBEc"
    ],
    "title": [
      "LC20lb",
      "MBeuO",
      "DKV0Md"
    ],
    "link": [
      "yuRUbf"
    ],
    "text": [
      "VwiC3b",
      "yXK7lf",
      "MUxGbd",
      "yDYNvb",
      "yDYNvb",
      "lEBKkf"
    ]
  }
}
```

### AI Iteration Pattern
Write script to make and analyse page structure, find scape classes for data and data units and then scrape page
and test if correct.  If not correct use another earlier or later attribute value from the stack until correct.

Tasks:
- update get page structure script to save link as text

