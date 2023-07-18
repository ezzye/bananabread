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
      "lyLwlc",
      "lEBKkf"
    ]
  }
}
```