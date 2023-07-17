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
Write python script to iterate through page structure json file  and find example texts and links in page structure and suggest css identifiers for each item and common to data units

Example input extract of page structure as json:
```json
[{
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
        "id": "topstuff"
      },
      "text": null,
      "link": "None",
      "children": []
    },
    {
      "tag": "div",
      "attributes": {
        "id": "search"
      },
      "text": null,
      "link": "None",
      "children": [
        {
          "tag": "div",
          "attributes": {
            "data-hveid": "CAMQGA"
          },
          "text": null,
          "link": "None",
          "children": [
            {
              "tag": "h1",
              "attributes": {
                "class": [
                  "Uo8X3b",
                  "OhScic",
                  "zsYMMe"
                ]
              },
              "text": "Search Results",
              "link": "None",
              "children": []
            },
            {
              "tag": "div",
              "attributes": {
                "class": [
                  "v7W49e"
                ],
                "id": "rso"
              },
              "text": null,
              "link": "None",
              "children": [
                {
                  "tag": "div",
                  "attributes": {
                    "class": [
                      "MjjYud"
                    ]
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
                        "data-hveid": "CBIQAA"
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
                                      "text": "Marc Bolan - N16\nLondon Remembers\nhttps://www.londonremembers.com \u203a memorials \u203a ma...",
                                      "link": "{'https://www.londonremembers.com/memorials/marc-bolan-n16'}",
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
                                          "text": "Marc Bolan - N16",
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
                                                  "text": "London Remembers",
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
                                                          "text": "\u203a memorials \u203a ma...",
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
                                                  "text": "London Remembers",
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
                                                          "text": "\u203a memorials \u203a ma...",
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
                                      "text": "Site: Marc Bolan - N16 (1 memorial). N16, Stoke Newington Common, 25. This is the penultimate house in the terrace before Maury Road, to the left.",
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
                      "tag": "span",
                      "attributes": {
                        "id": "z9PoV"
                      },
                      "text": "",
                      "link": "None",
                      "children": []
                    }
                  ]
                },
                {
                  "tag": "div",
                  "attributes": {
                    "class": [
                      "hlcw0c"
                    ]
                  },
                  "text": null,
                  "link": "None",
                  "children": [
                    {
                      "tag": "div",
                      "attributes": {
                        "class": [
                          "MjjYud"
                        ]
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
                    }
                  ]
                },
                {
                  "tag": "div",
                  "attributes": {
                    "class": [
                      "MjjYud"
                    ]
                  },
                  "text": null,
                  "link": "None",
                  "children": [
                    {
                      "tag": "div",
                      "attributes": {
                        "jscontroller": "Da4hkd",
                        "jsname": "bq0EGf",
                        "class": [
                          "cUnQKe"
                        ],
                        "data-smqc": "4",
                        "data-ulkwtsb": "1",
                        "data-hveid": "CBcQAA"
                      },
                      "text": null,
                      "link": "None",
                      "children": [
                        {
                          "tag": "div",
                          "attributes": {
                            "class": [
                              "Wt5Tfe"
                            ]
                          },
                          "text": null,
                          "link": "None",
                          "children": [
                            {
                              "tag": "div",
                              "attributes": {
                                "class": [
                                  "eJH8qe",
                                  "adDDi"
                                ]
                              },
                              "text": null,
                              "link": "None",
                              "children": [
                                {
                                  "tag": "div",
                                  "attributes": {
                                    "class": [
                                      "T6zPgb"
                                    ]
                                  },
                                  "text": null,
                                  "link": "None",
                                  "children": [
                                    {
                                      "tag": "div",
                                      "attributes": {
                                        "aria-level": "2",
                                        "role": "heading"
                                      },
                                      "text": null,
                                      "link": "None",
                                      "children": [
                                        {
                                          "tag": "span",
                                          "attributes": {
                                            "class": [
                                              "mgAbYb",
                                              "OSrXXb",
                                              "RES9jf",
                                              "IFnjPb"
                                            ]
                                          },
                                          "text": "People also ask",
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
                                    "class": [
                                      "YR2tRd"
                                    ]
                                  },
                                  "text": "You will see more English now.",
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
                                          "attributes": {},
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
                                                  "lUn2nc",
                                                  "eY4mx"
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
                                                      "IjabWd"
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
                                        },
                                        {
                                          "tag": "g-snackbar",
                                          "attributes": {
                                            "jsname": "t1F84b",
                                            "jscontroller": "OZLguc",
                                            "jsshadow": ""
                                          },
                                          "text": null,
                                          "link": "None",
                                          "children": [
                                            {
                                              "tag": "div",
                                              "attributes": {
                                                "jsname": "sM5MNb",
                                                "aria-live": "polite",
                                                "class": [
                                                  "LH3wG"
                                                ]
                                              },
                                              "text": null,
                                              "link": "None",
                                              "children": [
                                                {
                                                  "tag": "div",
                                                  "attributes": {
                                                    "jsname": "Ng57nc",
                                                    "class": [
                                                      "yK6jqe"
                                                    ]
                                                  },
                                                  "text": null,
                                                  "link": "None",
                                                  "children": [
                                                    {
                                                      "tag": "div",
                                                      "attributes": {
                                                        "class": [
                                                          "b77HKf"
                                                        ]
                                                      },
                                                      "text": null,
                                                      "link": "None",
                                                      "children": [
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "class": [
                                                              "rIxsve"
                                                            ],
                                                            "jsslot": ""
                                                          },
                                                          "text": null,
                                                          "link": "None",
                                                          "children": [
                                                            {
                                                              "tag": "span",
                                                              "attributes": {
                                                                "class": [
                                                                  "Txngnb",
                                                                  "wHYlTd",
                                                                  "yUTMj"
                                                                ]
                                                              },
                                                              "text": "You will see more English now.",
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
                                    }
                                  ]
                                }
                              ]
                            },
                            {
                              "tag": "div",
                              "attributes": {
                                "jsname": "N760b",
                                "data-sgrd": "true"
                              },
                              "text": null,
                              "link": "None",
                              "children": [
                                {
                                  "tag": "div",
                                  "attributes": {
                                    "jsname": "yEVEwb"
                                  },
                                  "text": null,
                                  "link": "None",
                                  "children": [
                                    {
                                      "tag": "div",
                                      "attributes": {},
                                      "text": null,
                                      "link": "None",
                                      "children": [
                                        {
                                          "tag": "div",
                                          "attributes": {
                                            "class": [
                                              "wQiwMc",
                                              "related-question-pair"
                                            ],
                                            "jscontroller": "xfmZMb"
                                          },
                                          "text": null,
                                          "link": "None",
                                          "children": [
                                            {
                                              "tag": "div",
                                              "attributes": {
                                                "jsname": "YrZdPb",
                                                "class": [
                                                  "HYvwY",
                                                  "ilulF",
                                                  "roMIYb",
                                                  "oST1qe",
                                                  "g7pt6d",
                                                  "h373nd"
                                                ],
                                                "jscontroller": "aD8OEe",
                                                "data-dic": "",
                                                "data-g": "",
                                                "data-ullb": "",
                                                "jsshadow": ""
                                              },
                                              "text": null,
                                              "link": "None",
                                              "children": [
                                                {
                                                  "tag": "div",
                                                  "attributes": {
                                                    "jsname": "clz4Ic",
                                                    "class": [
                                                      "ysxiae",
                                                      "iRPzcb"
                                                    ]
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
                                                      "tag": "div",
                                                      "attributes": {
                                                        "role": "button",
                                                        "tabindex": "0",
                                                        "jsaction": "AWEk5c",
                                                        "jsname": "tJHJj",
                                                        "class": [
                                                          "dnXCYb"
                                                        ],
                                                        "aria-expanded": "false",
                                                        "data-hveid": "CCgQAQ"
                                                      },
                                                      "text": null,
                                                      "link": "None",
                                                      "children": [
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "jsname": "lN6iy",
                                                            "class": [
                                                              "JlqpRe"
                                                            ]
                                                          },
                                                          "text": null,
                                                          "link": "None",
                                                          "children": [
                                                            {
                                                              "tag": "span",
                                                              "attributes": {
                                                                "class": [
                                                                  "JCzEY",
                                                                  "ZwRhJd"
                                                                ]
                                                              },
                                                              "text": "Where did Marc Bolan live in Hackney?",
                                                              "link": "None",
                                                              "children": [
                                                                {
                                                                  "tag": "span",
                                                                  "attributes": {
                                                                    "class": [
                                                                      "CSkcDe"
                                                                    ]
                                                                  },
                                                                  "text": "Where did Marc Bolan live in Hackney?",
                                                                  "link": "None",
                                                                  "children": []
                                                                }
                                                              ]
                                                            }
                                                          ]
                                                        },
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "jsname": "Q8Kwad",
                                                            "class": [
                                                              "aj35ze"
                                                            ]
                                                          },
                                                          "text": null,
                                                          "link": "None",
                                                          "children": []
                                                        },
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "jsname": "pcRaIe",
                                                            "class": [
                                                              "L3Ezfd"
                                                            ]
                                                          },
                                                          "text": null,
                                                          "link": "None",
                                                          "children": []
                                                        },
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "jsname": "gwzXIc",
                                                            "class": [
                                                              "ru2Kjc"
                                                            ]
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
                                                  "attributes": {
                                                    "jsname": "NRdf4c",
                                                    "class": [
                                                      "bCOlv"
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
                                    }
                                  ]
                                },
                                {
                                  "tag": "div",
                                  "attributes": {
                                    "jsname": "yEVEwb"
                                  },
                                  "text": null,
                                  "link": "None",
                                  "children": [
                                    {
                                      "tag": "div",
                                      "attributes": {},
                                      "text": null,
                                      "link": "None",
                                      "children": [
                                        {
                                          "tag": "div",
                                          "attributes": {
                                            "class": [
                                              "wQiwMc",
                                              "related-question-pair"
                                            ],
                                            "jscontroller": "xfmZMb"
                                          },
                                          "text": null,
                                          "link": "None",
                                          "children": [
                                            {
                                              "tag": "div",
                                              "attributes": {
                                                "jsname": "YrZdPb",
                                                "class": [
                                                  "HYvwY",
                                                  "ilulF",
                                                  "roMIYb",
                                                  "oST1qe",
                                                  "g7pt6d",
                                                  "h373nd"
                                                ],
                                                "jscontroller": "aD8OEe",
                                                "data-dic": "",
                                                "data-g": "",
                                                "data-ullb": "",
                                                "jsshadow": ""
                                              },
                                              "text": null,
                                              "link": "None",
                                              "children": [
                                                {
                                                  "tag": "div",
                                                  "attributes": {
                                                    "jsname": "clz4Ic",
                                                    "class": [
                                                      "ysxiae",
                                                      "iRPzcb"
                                                    ]
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
                                                      "tag": "div",
                                                      "attributes": {
                                                        "role": "button",
                                                        "tabindex": "0",
                                                        "jsaction": "AWEk5c",
                                                        "jsname": "tJHJj",
                                                        "class": [
                                                          "dnXCYb"
                                                        ],
                                                        "aria-expanded": "false",
                                                        "data-hveid": "CCMQAQ"
                                                      },
                                                      "text": null,
                                                      "link": "None",
                                                      "children": [
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "jsname": "lN6iy",
                                                            "class": [
                                                              "JlqpRe"
                                                            ]
                                                          },
                                                          "text": null,
                                                          "link": "None",
                                                          "children": [
                                                            {
                                                              "tag": "span",
                                                              "attributes": {
                                                                "class": [
                                                                  "JCzEY",
                                                                  "ZwRhJd"
                                                                ]
                                                              },
                                                              "text": "Where did Marc Bolan live in London?",
                                                              "link": "None",
                                                              "children": [
                                                                {
                                                                  "tag": "span",
                                                                  "attributes": {
                                                                    "class": [
                                                                      "CSkcDe"
                                                                    ]
                                                                  },
                                                                  "text": "Where did Marc Bolan live in London?",
                                                                  "link": "None",
                                                                  "children": []
                                                                }
                                                              ]
                                                            }
                                                          ]
                                                        },
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "jsname": "Q8Kwad",
                                                            "class": [
                                                              "aj35ze"
                                                            ]
                                                          },
                                                          "text": null,
                                                          "link": "None",
                                                          "children": []
                                                        },
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "jsname": "pcRaIe",
                                                            "class": [
                                                              "L3Ezfd"
                                                            ]
                                                          },
                                                          "text": null,
                                                          "link": "None",
                                                          "children": []
                                                        },
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "jsname": "gwzXIc",
                                                            "class": [
                                                              "ru2Kjc"
                                                            ]
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
                                                  "attributes": {
                                                    "jsname": "NRdf4c",
                                                    "class": [
                                                      "bCOlv"
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
                                    }
                                  ]
                                },
                                {
                                  "tag": "div",
                                  "attributes": {
                                    "jsname": "yEVEwb"
                                  },
                                  "text": null,
                                  "link": "None",
                                  "children": [
                                    {
                                      "tag": "div",
                                      "attributes": {},
                                      "text": null,
                                      "link": "None",
                                      "children": [
                                        {
                                          "tag": "div",
                                          "attributes": {
                                            "class": [
                                              "wQiwMc",
                                              "related-question-pair"
                                            ],
                                            "jscontroller": "xfmZMb"
                                          },
                                          "text": null,
                                          "link": "None",
                                          "children": [
                                            {
                                              "tag": "div",
                                              "attributes": {
                                                "jsname": "YrZdPb",
                                                "class": [
                                                  "HYvwY",
                                                  "ilulF",
                                                  "roMIYb",
                                                  "oST1qe",
                                                  "g7pt6d",
                                                  "h373nd"
                                                ],
                                                "jscontroller": "aD8OEe",
                                                "data-dic": "",
                                                "data-g": "",
                                                "data-ullb": "",
                                                "jsshadow": ""
                                              },
                                              "text": null,
                                              "link": "None",
                                              "children": [
                                                {
                                                  "tag": "div",
                                                  "attributes": {
                                                    "jsname": "clz4Ic",
                                                    "class": [
                                                      "ysxiae",
                                                      "iRPzcb"
                                                    ]
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
                                                      "tag": "div",
                                                      "attributes": {
                                                        "role": "button",
                                                        "tabindex": "0",
                                                        "jsaction": "AWEk5c",
                                                        "jsname": "tJHJj",
                                                        "class": [
                                                          "dnXCYb"
                                                        ],
                                                        "aria-expanded": "false",
                                                        "data-hveid": "CBkQAQ"
                                                      },
                                                      "text": null,
                                                      "link": "None",
                                                      "children": [
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "jsname": "lN6iy",
                                                            "class": [
                                                              "JlqpRe"
                                                            ]
                                                          },
                                                          "text": null,
                                                          "link": "None",
                                                          "children": [
                                                            {
                                                              "tag": "span",
                                                              "attributes": {
                                                                "class": [
                                                                  "JCzEY",
                                                                  "ZwRhJd"
                                                                ]
                                                              },
                                                              "text": "Where is Mark Boland buried?",
                                                              "link": "None",
                                                              "children": [
                                                                {
                                                                  "tag": "span",
                                                                  "attributes": {
                                                                    "class": [
                                                                      "CSkcDe"
                                                                    ]
                                                                  },
                                                                  "text": "Where is Mark Boland buried?",
                                                                  "link": "None",
                                                                  "children": []
                                                                }
                                                              ]
                                                            }
                                                          ]
                                                        },
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "jsname": "Q8Kwad",
                                                            "class": [
                                                              "aj35ze"
                                                            ]
                                                          },
                                                          "text": null,
                                                          "link": "None",
                                                          "children": []
                                                        },
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "jsname": "pcRaIe",
                                                            "class": [
                                                              "L3Ezfd"
                                                            ]
                                                          },
                                                          "text": null,
                                                          "link": "None",
                                                          "children": []
                                                        },
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "jsname": "gwzXIc",
                                                            "class": [
                                                              "ru2Kjc"
                                                            ]
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
                                                  "attributes": {
                                                    "jsname": "NRdf4c",
                                                    "class": [
                                                      "bCOlv"
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
                                    }
                                  ]
                                },
                                {
                                  "tag": "div",
                                  "attributes": {
                                    "jsname": "yEVEwb"
                                  },
                                  "text": null,
                                  "link": "None",
                                  "children": [
                                    {
                                      "tag": "div",
                                      "attributes": {},
                                      "text": null,
                                      "link": "None",
                                      "children": [
                                        {
                                          "tag": "div",
                                          "attributes": {
                                            "class": [
                                              "wQiwMc",
                                              "related-question-pair"
                                            ],
                                            "jscontroller": "xfmZMb"
                                          },
                                          "text": null,
                                          "link": "None",
                                          "children": [
                                            {
                                              "tag": "div",
                                              "attributes": {
                                                "jsname": "YrZdPb",
                                                "class": [
                                                  "HYvwY",
                                                  "ilulF",
                                                  "roMIYb",
                                                  "oST1qe",
                                                  "g7pt6d",
                                                  "h373nd"
                                                ],
                                                "jscontroller": "aD8OEe",
                                                "data-dic": "",
                                                "data-g": "",
                                                "data-ullb": "",
                                                "jsshadow": ""
                                              },
                                              "text": null,
                                              "link": "None",
                                              "children": [
                                                {
                                                  "tag": "div",
                                                  "attributes": {
                                                    "jsname": "clz4Ic",
                                                    "class": [
                                                      "ysxiae",
                                                      "iRPzcb"
                                                    ]
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
                                                      "tag": "div",
                                                      "attributes": {
                                                        "role": "button",
                                                        "tabindex": "0",
                                                        "jsaction": "AWEk5c",
                                                        "jsname": "tJHJj",
                                                        "class": [
                                                          "dnXCYb"
                                                        ],
                                                        "aria-expanded": "false",
                                                        "data-hveid": "CCUQAQ"
                                                      },
                                                      "text": null,
                                                      "link": "None",
                                                      "children": [
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "jsname": "lN6iy",
                                                            "class": [
                                                              "JlqpRe"
                                                            ]
                                                          },
                                                          "text": null,
                                                          "link": "None",
                                                          "children": [
                                                            {
                                                              "tag": "span",
                                                              "attributes": {
                                                                "class": [
                                                                  "JCzEY",
                                                                  "ZwRhJd"
                                                                ]
                                                              },
                                                              "text": "Where is the tree where Marc Bolan died?",
                                                              "link": "None",
                                                              "children": [
                                                                {
                                                                  "tag": "span",
                                                                  "attributes": {
                                                                    "class": [
                                                                      "CSkcDe"
                                                                    ]
                                                                  },
                                                                  "text": "Where is the tree where Marc Bolan died?",
                                                                  "link": "None",
                                                                  "children": []
                                                                }
                                                              ]
                                                            }
                                                          ]
                                                        },
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "jsname": "Q8Kwad",
                                                            "class": [
                                                              "aj35ze"
                                                            ]
                                                          },
                                                          "text": null,
                                                          "link": "None",
                                                          "children": []
                                                        },
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "jsname": "pcRaIe",
                                                            "class": [
                                                              "L3Ezfd"
                                                            ]
                                                          },
                                                          "text": null,
                                                          "link": "None",
                                                          "children": []
                                                        },
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "jsname": "gwzXIc",
                                                            "class": [
                                                              "ru2Kjc"
                                                            ]
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
                                                  "attributes": {
                                                    "jsname": "NRdf4c",
                                                    "class": [
                                                      "bCOlv"
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
                                    }
                                  ]
                                },
                                {
                                  "tag": "div",
                                  "attributes": {
                                    "jsname": "grQLgb",
                                    "class": [
                                      "yp"
                                    ],
                                    "data-async-fcv": "3",
                                    "data-async-ons": "10041",
                                    "id": "fc_1"
                                  },
                                  "text": null,
                                  "link": "None",
                                  "children": []
                                },
                                {
                                  "tag": "g-loading-icon",
                                  "attributes": {
                                    "jsname": "aZ2wEe",
                                    "class": [
                                      "uKh9yc",
                                      "S3PB2d"
                                    ]
                                  },
                                  "text": null,
                                  "link": "None",
                                  "children": [
                                    {
                                      "tag": "img",
                                      "attributes": {
                                        "height": "24",
                                        "width": "24",
                                        "alt": "Loading..."
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
                              "attributes": {
                                "class": [
                                  "XVdSCb",
                                  "KFFQ0c",
                                  "xKf9F"
                                ]
                              },
                              "text": null,
                              "link": "None",
                              "children": [
                                {
                                  "tag": "div",
                                  "attributes": {
                                    "class": [
                                      "akqY6"
                                    ]
                                  },
                                  "text": null,
                                  "link": "None",
                                  "children": []
                                },
                                {
                                  "tag": "div",
                                  "attributes": {
                                    "class": [
                                      "YfftMc"
                                    ]
                                  },
                                  "text": null,
                                  "link": "None",
                                  "children": [
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
                                            "id": "duf3-44",
                                            "data-jiis": "up",
                                            "data-async-type": "duffy3",
                                            "class": [
                                              "yp"
                                            ]
                                          },
                                          "text": null,
                                          "link": "None",
                                          "children": []
                                        },
                                        {
                                          "tag": "a",
                                          "attributes": {
                                            "class": [
                                              "oBa0Fe"
                                            ],
                                            "href": "#",
                                            "data-async-trigger": "duf3-44",
                                            "role": "button"
                                          },
                                          "text": "Feedback",
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
                      ]
                    }
                  ]
                },
                {
                  "tag": "div",
                  "attributes": {
                    "class": [
                      "MjjYud"
                    ]
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
                        "data-hveid": "CBEQAA"
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
                                      "text": "Marc Bolan London's First Glam-Rock Star\nKnowledgeoflondon.com\nhttp://knowledgeoflondon.com \u203a marcbolan",
                                      "link": "{'http://knowledgeoflondon.com/marcbolan.html'}",
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
                                          "text": "Marc Bolan London's First Glam-Rock Star",
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
                                                  "text": "Knowledgeoflondon.com",
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
                                                          "text": "\u203a marcbolan",
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
                                                  "text": "Knowledgeoflondon.com",
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
                                                          "text": "\u203a marcbolan",
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
                                      "text": "Marc Bolan was born Mark Feld on 30 September 1947, at 25a Stoke Newington Common, where he lived up until 1962 with his mother, Phyllis, who worked on a Soho\u00a0...",
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
                },
                {
                  "tag": "div",
                  "attributes": {
                    "class": [
                      "MjjYud"
                    ]
                  },
                  "text": null,
                  "link": "None",
                  "children": [
                    {
                      "tag": "span",
                      "attributes": {
                        "class": [
                          "oUAcPd"
                        ],
                        "id": "fld_1"
                      },
                      "text": "",
                      "link": "None",
                      "children": []
                    },
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
                        "data-hveid": "CDkQAA"
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
                                      "text": "Marc Bolan - The Early Years\nMarc Bolan Net\nhttps://www.marc-bolan.net \u203a biography \u203a biography-1",
                                      "link": "{'https://www.marc-bolan.net/biography/biography-1.html'}",
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
                                          "text": "Marc Bolan - The Early Years",
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
                                                  "text": "Marc Bolan Net",
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
                                                          "text": "\u203a biography \u203a biography-1",
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
                                                  "text": "Marc Bolan Net",
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
                                                          "text": "\u203a biography \u203a biography-1",
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
                                      "text": "The family lived in flat in a terraced house at 25 Stoke Newington Common, Hackney (see right) and Marc lived there from his birth to the age of fourteen.",
                                      "link": "None",
                                      "children": [
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
                                          "text": "Marc",
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
                },
                {
                  "tag": "div",
                  "attributes": {
                    "class": [
                      "MjjYud"
                    ]
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
                        "data-hveid": "CD0QAA"
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
                                      "text": "Marc Bolan - N16 | Plaques of London\nPlaques of London\nhttps://www.plaquesoflondon.co.uk \u203a locations \u203a marc...",
                                      "link": "{'https://www.plaquesoflondon.co.uk/locations/marcc-bolan-n16/'}",
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
                                          "text": "Marc Bolan - N16 | Plaques of London",
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
                                                  "text": "Plaques of London",
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
                                                          "text": "\u203a locations \u203a marc...",
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
                                                  "text": "Plaques of London",
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
                                                          "text": "\u203a locations \u203a marc...",
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
                                      "text": "Marc Bolan - N16. Musician. Born 30th September 1947. Died 16th September 1977. Location 25 Stoke Newington Common, London, N16. Categories.",
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
                },
                {
                  "tag": "div",
                  "attributes": {
                    "class": [
                      "MjjYud"
                    ]
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
                        "data-hveid": "CDsQAA"
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
                                      "text": "Born to boogie \u2013 a look at Marc Bolan's early life in Hackney\nHackney Citizen\nhttps://www.hackneycitizen.co.uk \u203a 2017/09/15 \u203a mar...",
                                      "link": "{'https://www.hackneycitizen.co.uk/2017/09/15/marc-bolan-hackney-childhood/'}",
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
                                          "text": "Born to boogie \u2013 a look at Marc Bolan's early life in Hackney",
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
                                                  "text": "Hackney Citizen",
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
                                                          "text": "\u203a 2017/09/15 \u203a mar...",
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
                                                  "text": "Hackney Citizen",
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
                                                          "text": "\u203a 2017/09/15 \u203a mar...",
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
                                      "attributes": {
                                        "class": [
                                          "MUxGbd",
                                          "wuQ4Ob",
                                          "WZ8Tjf"
                                        ]
                                      },
                                      "text": "15 Sept 2017 \u2014",
                                      "link": "None",
                                      "children": [
                                        {
                                          "tag": "span",
                                          "attributes": {},
                                          "text": "15 Sept 2017",
                                          "link": "None",
                                          "children": []
                                        }
                                      ]
                                    },
                                    {
                                      "tag": "span",
                                      "attributes": {},
                                      "text": "Bolan pioneered glam rock with T-Rex (Formerly Tyrannosaurus Rex) inspiring a ... In 1947, Stoke Newington was only just recovering from the\u00a0...",
                                      "link": "None",
                                      "children": [
                                        {
                                          "tag": "em",
                                          "attributes": {},
                                          "text": "T-Rex",
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
                },
                {
                  "tag": "div",
                  "attributes": {
                    "class": [
                      "MjjYud"
                    ]
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
                        "data-hveid": "CDoQAA"
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
                                      "text": "Marc Bolan lived here - London\nShady Old Lady\nhttps://www.shadyoldlady.com \u203a location",
                                      "link": "{'https://www.shadyoldlady.com/location/1020'}",
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
                                          "text": "Marc Bolan lived here - London",
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
                                                  "text": "Shady Old Lady",
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
                                                          "text": "\u203a location",
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
                                                  "text": "Shady Old Lady",
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
                                                          "text": "\u203a location",
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
                                      "text": "Location: 25 Stoke Newington Common, Hackney Description: The son of a Jewish van driver and caretaker, Bolan grew up as Marc Feld here in post-war Hackney\u00a0...",
                                      "link": "None",
                                      "children": [
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
                                          "text": "Bolan",
                                          "link": "None",
                                          "children": []
                                        },
                                        {
                                          "tag": "em",
                                          "attributes": {},
                                          "text": "Marc",
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
                },
                {
                  "tag": "div",
                  "attributes": {
                    "class": [
                      "MjjYud"
                    ]
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
                        "data-hveid": "CDIQAA"
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
                                      "text": "Marc Bolan's childhood home, Stoke Newington Common\nFlickr\nhttps://www.flickr.com \u203a photos \u203a albedo",
                                      "link": "{'https://www.flickr.com/photos/albedo/263135528'}",
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
                                          "text": "Marc Bolan's childhood home, Stoke Newington Common",
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
                                                  "text": "Flickr",
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
                                                          "text": "\u203a photos \u203a albedo",
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
                                                  "text": "Flickr",
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
                                                          "text": "\u203a photos \u203a albedo",
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
                                      "text": "Marc Bolan's childhood home, Stoke Newington Common. Born Mark Feld in 1947at Hackney Hospital, he lived here from then until 1962.",
                                      "link": "None",
                                      "children": [
                                        {
                                          "tag": "em",
                                          "attributes": {},
                                          "text": "Marc Bolan's",
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
                },
                {
                  "tag": "div",
                  "attributes": {
                    "class": [
                      "MjjYud"
                    ]
                  },
                  "text": null,
                  "link": "None",
                  "children": [
                    {
                      "tag": "div",
                      "attributes": {},
                      "text": null,
                      "link": "None",
                      "children": [
                        {
                          "tag": "div",
                          "attributes": {
                            "jsname": "pKB8Bc",
                            "class": [
                              "g",
                              "dFd2Tb",
                              "PhX2wd"
                            ],
                            "data-hveid": "CDYQAA"
                          },
                          "text": null,
                          "link": "None",
                          "children": [
                            {
                              "tag": "div",
                              "attributes": {},
                              "text": null,
                              "link": "None",
                              "children": [
                                {
                                  "tag": "div",
                                  "attributes": {},
                                  "text": null,
                                  "link": "None",
                                  "children": [
                                    {
                                      "tag": "div",
                                      "attributes": {
                                        "class": [
                                          "ct3b9e"
                                        ]
                                      },
                                      "text": null,
                                      "link": "None",
                                      "children": [
                                        {
                                          "tag": "div",
                                          "attributes": {
                                            "class": [
                                              "DhN8Cf"
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
                                              "text": "On this day in 1947, Marc Bolan of T. Rex is born Mark Feld in ...\nFacebook\nhttps://www.facebook.com \u203a ... \u203a Videos",
                                              "link": "{'https://www.facebook.com/MonstersOfRockOfficial/videos/on-this-day-in-1947-marc-bolan-of-t-rex-is-born-mark-feld-in-stoke-newington-lon/988177001746973/'}",
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
                                                  "text": "On this day in 1947, Marc Bolan of T. Rex is born Mark Feld in ...",
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
                                                          "text": "Facebook",
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
                                                                  "text": "\u203a ... \u203a Videos",
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
                                                          "text": "Facebook",
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
                                                                  "text": "\u203a ... \u203a Videos",
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
                                          "dXiKIc"
                                        ],
                                        "jsshadow": ""
                                      },
                                      "text": null,
                                      "link": "None",
                                      "children": [
                                        {
                                          "tag": "a",
                                          "attributes": {},
                                          "text": "0:06",
                                          "link": "{'https://www.facebook.com/MonstersOfRockOfficial/videos/on-this-day-in-1947-marc-bolan-of-t-rex-is-born-mark-feld-in-stoke-newington-lon/988177001746973/'}",
                                          "children": [
                                            {
                                              "tag": "div",
                                              "attributes": {
                                                "class": [
                                                  "yZvQec"
                                                ],
                                                "aria-hidden": "true"
                                              },
                                              "text": null,
                                              "link": "None",
                                              "children": [
                                                {
                                                  "tag": "div",
                                                  "attributes": {
                                                    "class": [
                                                      "AZJdrc",
                                                      "t7VAxe",
                                                      "zGXzeb"
                                                    ]
                                                  },
                                                  "text": null,
                                                  "link": "None",
                                                  "children": [
                                                    {
                                                      "tag": "div",
                                                      "attributes": {
                                                        "class": [
                                                          "uhHOwf",
                                                          "BYbUcd"
                                                        ]
                                                      },
                                                      "text": null,
                                                      "link": "None",
                                                      "children": [
                                                        {
                                                          "tag": "img",
                                                          "attributes": {
                                                            "alt": "",
                                                            "id": "dimg_1",
                                                            "data-deferred": "1"
                                                          },
                                                          "text": null,
                                                          "link": "None",
                                                          "children": []
                                                        }
                                                      ]
                                                    },
                                                    {
                                                      "tag": "div",
                                                      "attributes": {
                                                        "class": [
                                                          "kSFuOd",
                                                          "rkqHyd"
                                                        ],
                                                        "aria-hidden": "true"
                                                      },
                                                      "text": null,
                                                      "link": "None",
                                                      "children": [
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "class": [
                                                              "Ylm8Fc",
                                                              "YmeD8e"
                                                            ]
                                                          },
                                                          "text": null,
                                                          "link": "None",
                                                          "children": [
                                                            {
                                                              "tag": "span",
                                                              "attributes": {
                                                                "class": [
                                                                  "hDVnsf",
                                                                  "z1asCe"
                                                                ],
                                                                "aria-hidden": "true"
                                                              },
                                                              "text": "",
                                                              "link": "None",
                                                              "children": []
                                                            }
                                                          ]
                                                        },
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "class": [
                                                              "c8rnLc",
                                                              "flgn0c",
                                                              "zCaigb"
                                                            ],
                                                            "aria-label": "6 seconds"
                                                          },
                                                          "text": null,
                                                          "link": "None",
                                                          "children": [
                                                            {
                                                              "tag": "span",
                                                              "attributes": {
                                                                "class": [
                                                                  "JIv15d"
                                                                ]
                                                              },
                                                              "text": "0:06",
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
                                              "mSA5Bd"
                                            ]
                                          },
                                          "text": null,
                                          "link": "None",
                                          "children": [
                                            {
                                              "tag": "div",
                                              "attributes": {
                                                "class": [
                                                  "Uroaid"
                                                ]
                                              },
                                              "text": null,
                                              "link": "None",
                                              "children": [
                                                {
                                                  "tag": "b",
                                                  "attributes": {},
                                                  "text": null,
                                                  "link": "None",
                                                  "children": []
                                                },
                                                {
                                                  "tag": "b",
                                                  "attributes": {},
                                                  "text": null,
                                                  "link": "None",
                                                  "children": []
                                                },
                                                {
                                                  "tag": "b",
                                                  "attributes": {},
                                                  "text": null,
                                                  "link": "None",
                                                  "children": []
                                                }
                                              ]
                                            },
                                            {
                                              "tag": "div",
                                              "attributes": {
                                                "class": [
                                                  "P7xzyf"
                                                ]
                                              },
                                              "text": null,
                                              "link": "None",
                                              "children": [
                                                {
                                                  "tag": "span",
                                                  "attributes": {
                                                    "class": [
                                                      "Zg1NU"
                                                    ]
                                                  },
                                                  "text": "Facebook",
                                                  "link": "None",
                                                  "children": []
                                                },
                                                {
                                                  "tag": "span",
                                                  "attributes": {},
                                                  "text": "MONSTERS OF ROCK",
                                                  "link": "None",
                                                  "children": []
                                                },
                                                {
                                                  "tag": "span",
                                                  "attributes": {},
                                                  "text": "30 Sept 2021",
                                                  "link": "None",
                                                  "children": [
                                                    {
                                                      "tag": "span",
                                                      "attributes": {},
                                                      "text": "30 Sept 2021",
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
                                    },
                                    {
                                      "tag": "div",
                                      "attributes": {
                                        "class": [
                                          "WKugpe"
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
                        }
                      ]
                    }
                  ]
                },
                {
                  "tag": "div",
                  "attributes": {
                    "class": [
                      "hlcw0c"
                    ]
                  },
                  "text": null,
                  "link": "None",
                  "children": [
                    {
                      "tag": "div",
                      "attributes": {
                        "class": [
                          "MjjYud"
                        ]
                      },
                      "text": null,
                      "link": "None",
                      "children": [
                        {
                          "tag": "div",
                          "attributes": {},
                          "text": null,
                          "link": "None",
                          "children": [
                            {
                              "tag": "div",
                              "attributes": {
                                "jsname": "pKB8Bc",
                                "class": [
                                  "g",
                                  "dFd2Tb",
                                  "PhX2wd"
                                ],
                                "data-hveid": "CDwQAA"
                              },
                              "text": null,
                              "link": "None",
                              "children": [
                                {
                                  "tag": "div",
                                  "attributes": {},
                                  "text": null,
                                  "link": "None",
                                  "children": [
                                    {
                                      "tag": "div",
                                      "attributes": {},
                                      "text": null,
                                      "link": "None",
                                      "children": [
                                        {
                                          "tag": "div",
                                          "attributes": {
                                            "class": [
                                              "ct3b9e"
                                            ]
                                          },
                                          "text": null,
                                          "link": "None",
                                          "children": [
                                            {
                                              "tag": "div",
                                              "attributes": {
                                                "class": [
                                                  "DhN8Cf"
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
                                                  "text": "A short trip to Stoke Newington Common, with \"Change\" of ...\nYouTube\nhttps://www.youtube.com \u203a watch",
                                                  "link": "{'https://www.youtube.com/watch?v=9ljW4FH4-gg'}",
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
                                                      "text": "A short trip to Stoke Newington Common, with \"Change\" of ...",
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
                                                              "text": "YouTube",
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
                                                                      "text": "\u203a watch",
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
                                                              "text": "YouTube",
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
                                                                      "text": "\u203a watch",
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
                                              "dXiKIc"
                                            ],
                                            "jscontroller": "CCowhf",
                                            "jsshadow": ""
                                          },
                                          "text": null,
                                          "link": "None",
                                          "children": [
                                            {
                                              "tag": "a",
                                              "attributes": {},
                                              "text": "3:35",
                                              "link": "{'https://www.youtube.com/watch?v=9ljW4FH4-gg'}",
                                              "children": [
                                                {
                                                  "tag": "div",
                                                  "attributes": {
                                                    "class": [
                                                      "yZvQec"
                                                    ],
                                                    "aria-hidden": "true"
                                                  },
                                                  "text": null,
                                                  "link": "None",
                                                  "children": [
                                                    {
                                                      "tag": "div",
                                                      "attributes": {
                                                        "class": [
                                                          "AZJdrc",
                                                          "t7VAxe",
                                                          "zGXzeb"
                                                        ]
                                                      },
                                                      "text": null,
                                                      "link": "None",
                                                      "children": [
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "class": [
                                                              "uhHOwf",
                                                              "BYbUcd"
                                                            ]
                                                          },
                                                          "text": null,
                                                          "link": "None",
                                                          "children": [
                                                            {
                                                              "tag": "img",
                                                              "attributes": {
                                                                "alt": "",
                                                                "id": "dimg_3",
                                                                "data-deferred": "1"
                                                              },
                                                              "text": null,
                                                              "link": "None",
                                                              "children": []
                                                            }
                                                          ]
                                                        },
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "jsname": "DwcXhb",
                                                            "class": [
                                                              "LIna9b"
                                                            ],
                                                            "aria-hidden": "true"
                                                          },
                                                          "text": null,
                                                          "link": "None",
                                                          "children": [
                                                            {
                                                              "tag": "div",
                                                              "attributes": {
                                                                "class": [
                                                                  "VYkpsb"
                                                                ],
                                                                "jscontroller": "Fy1Pv",
                                                                "data-stfc": "1"
                                                              },
                                                              "text": null,
                                                              "link": "None",
                                                              "children": []
                                                            }
                                                          ]
                                                        },
                                                        {
                                                          "tag": "div",
                                                          "attributes": {
                                                            "class": [
                                                              "kSFuOd",
                                                              "rkqHyd"
                                                            ],
                                                            "aria-hidden": "true"
                                                          },
                                                          "text": null,
                                                          "link": "None",
                                                          "children": [
                                                            {
                                                              "tag": "div",
                                                              "attributes": {
                                                                "class": [
                                                                  "Ylm8Fc",
                                                                  "YmeD8e"
                                                                ]
                                                              },
                                                              "text": null,
                                                              "link": "None",
                                                              "children": [
                                                                {
                                                                  "tag": "span",
                                                                  "attributes": {
                                                                    "class": [
                                                                      "hDVnsf",
                                                                      "z1asCe"
                                                                    ],
                                                                    "aria-hidden": "true"
                                                                  },
                                                                  "text": "",
                                                                  "link": "None",
                                                                  "children": []
                                                                }
                                                              ]
                                                            },
                                                            {
                                                              "tag": "div",
                                                              "attributes": {
                                                                "class": [
                                                                  "c8rnLc",
                                                                  "flgn0c",
                                                                  "zCaigb"
                                                                ]
                                                              },
                                                              "text": null,
                                                              "link": "None",
                                                              "children": [
                                                                {
                                                                  "tag": "span",
                                                                  "attributes": {
                                                                    "class": [
                                                                      "JIv15d"
                                                                    ]
                                                                  },
                                                                  "text": "3:35",
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
                                                  "mSA5Bd"
                                                ]
                                              },
                                              "text": null,
                                              "link": "None",
                                              "children": [
                                                {
                                                  "tag": "div",
                                                  "attributes": {
                                                    "class": [
                                                      "Uroaid"
                                                    ]
                                                  },
                                                  "text": null,
                                                  "link": "None",
                                                  "children": [
                                                    {
                                                      "tag": "b",
                                                      "attributes": {},
                                                      "text": null,
                                                      "link": "None",
                                                      "children": []
                                                    },
                                                    {
                                                      "tag": "b",
                                                      "attributes": {},
                                                      "text": null,
                                                      "link": "None",
                                                      "children": []
                                                    }
                                                  ]
                                                },
                                                {
                                                  "tag": "div",
                                                  "attributes": {
                                                    "class": [
                                                      "P7xzyf"
                                                    ]
                                                  },
                                                  "text": null,
                                                  "link": "None",
                                                  "children": [
                                                    {
                                                      "tag": "span",
                                                      "attributes": {
                                                        "class": [
                                                          "Zg1NU"
                                                        ]
                                                      },
                                                      "text": "YouTube",
                                                      "link": "None",
                                                      "children": []
                                                    },
                                                    {
                                                      "tag": "span",
                                                      "attributes": {},
                                                      "text": "CosmicSlider",
                                                      "link": "None",
                                                      "children": []
                                                    },
                                                    {
                                                      "tag": "span",
                                                      "attributes": {},
                                                      "text": "11 Feb 2017",
                                                      "link": "None",
                                                      "children": [
                                                        {
                                                          "tag": "span",
                                                          "attributes": {},
                                                          "text": "11 Feb 2017",
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
                                        },
                                        {
                                          "tag": "div",
                                          "attributes": {
                                            "class": [
                                              "WKugpe"
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
    }
  ]
}]
```

Text example input as json:
```json
[
  {
  "title": "Marc Bolan - N16",
  "link": "https://www.londonremembers.com/memorials/marc-bolan-n16",
  "text": "Marc Bolan, born Mark Feld on 30/9/1947 grew up in London's Stoke Newington and lived in this house at 25 Stoke Newington CommonMarc Bolan, born Mark Feld on 30/9/1947 grew up in London's Stoke Newington and lived in this house at 25 Stoke Newington Common"
},
{
"title": "Marc Bolan's London House in Hackney",
"link": "https://www.hangerlondon.com/marc-bolan-london/",
"text": "Marc Bolan, born Mark Feld on 30/9/1947 grew up in London's Stoke Newington and lived in this house at 25 Stoke Newington Common."
}
]
```
Example output showing attribute values for title, link and text
```json
{
  "attributes": {
    "common values for each data item": [
      "g","Ww4FFb","vt6azd","tF2Cxc","asEBEc"
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
      "lyLwlc",
      "lEBKkf"
    ]
  }
}
```

