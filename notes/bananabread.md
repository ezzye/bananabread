# Banana Bread Idea

## AI Agent
The banana bread agent (BBA) is a simple AI agent that is designed to scrape the web and make daily, weekly or monthly newsletters.

BBA has the following parts:
- A web scraper
- A web scaper configuration file
- Web scaper outputs
- A memory json file that stores the success/falilure results of previous scrapes together with scraper configuration used for that result
- BBA planning prompts
- BBA decision prompts
- BBA agent control prompts

### Web scraper
The web scraper is a simple python script that uses the requests-html libraries to scrape the web. The web scraper is configured using a configuration file.

### Web scraper configuration file
- webpage_content.json
- data_unit.json
- common_parent_attributes.json

### Web scraper outputs
- webpage_content.json
- text_snippets

### Web scraper input
- urls
- urls options/query terms such as search terms
- page search terms:
 - page title
 - page description
 - page keywords
 - image alt text
 - image

### Memory json file
- memory.json, this contains:
 - success/failure of previous scrapes
 - related scraper configuration

### BBA agent control prompts
- for example, "This is relevant to EVERY prompt I ask.

no talk; just do

Task reading:
Before each response, read the current tasklist from "chatGPT_Todo.txt". Re prioritize the tasks, and assist me in getting started and completing the top task

Task creation & summary:
You must always summarize all previous messages, and break down our goals down into 3-10 step by step actions. Write code and save them to a text file named "chatGPT_Todo.txt". Always provide a download link.

Only after saving the task list and providing the download link,
provide Hotkeys
List 4 or more multiple choices.
Use these to ask questions and solicit any needed information, guess my possible responses or help me brainstorm alternate conversation paths. Get creative and suggest things I might not have thought of prior. The goal is create open mindedness and jog my thinking in a novel, insightful and helpful new way

w: to advance, yes
s: to slow down or stop, no
a or d: to change the vibe, or alter directionally

If you need to additional cases and variants.  Use double tap variants like ww or ss for strong agree or disagree are encouraged"

- use python script using openai 3.5 and 4 apis for agent with function calling and LanChain to make agent

### Newsletter notes
- use https://www.beehiiv.com/ to create newsletter

