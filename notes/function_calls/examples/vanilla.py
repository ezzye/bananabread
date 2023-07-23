#!/usr/bin/env python

import langchain
import openai
import json
from requests_html import HTMLSession
import requests

# Environment Variables
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY', 'YourAPIKeyIfNotSet')


def get_url(loc, language="en", form="json"):
    place = loc.replace(" ", "+")
    return f"https://geocoding-api.open-meteo.com/v1/search?name={place}&count=10&language={language}&format={form}"


def get_request(url):
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
        'Upgrade-Insecure-Requests': '1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
    }
    web_response = None  # Initialize web_response to None
    try:
        session = HTMLSession()
        # web_response = session.get(url, headers=headers)
        web_response = requests.get(url, headers=headers)

        # session.close()

    except requests.exceptions.RequestException as e:
        print(e)
    return web_response


def get_latitude_longitude(location):
    """Get the current lat and longitude for a given location name"""
    url = get_url(location)
    lat_json = get_request(url)
    return lat_json.json()


def find_most_matching_dict(checking_dict, dict_list):
    max_matches = 0
    most_matching_dict = None

    for d in dict_list:
        matches = sum(k in checking_dict and checking_dict[k] == v for k, v in d.items())
        if matches > max_matches:
            max_matches = matches
            most_matching_dict = d
    if max_matches < 2:
        print(f"max_matches {max_matches} not sure if this the location you want")
        most_matching_dict = None

    print(f"max_matches {max_matches}")

    return most_matching_dict


# APIs for weather see https://open-meteo.com/en/docs eg
# https://api.open-meteo.com/v1/forecast?latitude=51.56246&longitude=-0.07401&daily=temperature_2m_max,temperature_2m_min,sunrise,sunset,uv_index_max,precipitation_sum,rain_sum,showers_sum,precipitation_hours,precipitation_probability_max,windspeed_10m_max,windgusts_10m_max,winddirection_10m_dominant&windspeed_unit=mph&timezone=Europe%2FLondon
# {
#     "latitude": 51.56,
#     "longitude": -0.08000016,
#     "generationtime_ms": 0.9769201278686523,
#     "utc_offset_seconds": 3600,
#     "timezone": "Europe/London",
#     "timezone_abbreviation": "BST",
#     "elevation": 30.0,
#     "daily_units": {
#         "time": "iso8601",
#         "temperature_2m_max": "°C",
#         "temperature_2m_min": "°C",
#         "sunrise": "iso8601",
#         "sunset": "iso8601",
#         "uv_index_max": "",
#         "precipitation_sum": "mm",
#         "rain_sum": "mm",
#         "showers_sum": "mm",
#         "precipitation_hours": "h",
#         "precipitation_probability_max": "%",
#         "windspeed_10m_max": "mp/h",
#         "windgusts_10m_max": "mp/h",
#         "winddirection_10m_dominant": "°"
# }


# for geo location see https://open-meteo.com/en/docs/geocoding-api
# eg https://geocoding-api.open-meteo.com/v1/search?name=Stoke+Newington&count=10&language=en&format=json
# {
#     "results": [
#         {
#             "id": 2636843,
#             "name": "Stoke Newington",
#             "latitude": 51.56246,
#             "longitude": -0.07401,
#             "elevation": 28.0,
#             "feature_code": "PPLX",
#             "country_code": "GB",
#             "admin1_id": 6269131,
#             "admin2_id": 2648110,
#             "admin3_id": 3333148,
#             "timezone": "Europe/London",
#             "country_id": 2635167,
#             "country": "United Kingdom",
#             "admin1": "England",
#             "admin2": "Greater London",
#             "admin3": "Hackney"
#         },
#         {
#             "id": 2636844,
#             ...
#         }
#     ],
#     "generationtime_ms": 0.6699562
# }

function_descriptions = [
    {
        "name": "get_current_latitude_and_longitude",
        "description": "Get the current latitude and longitude for a given location name",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "The name of the location to get the latitude and longitude for. Eg 'Aston'",
                },
                "language": {
                    "type": "string",
                    "description": "ISO 639-1 code for the language to use. Eg 'en'",
                },
                "format": {
                    "type": "string",
                    "description": "format file extension Eg 'json' or 'csv",
                },
                "country": {
                    "type": "string",
                    "description": "name of the country in full NOT code to search in. Eg 'United Kingdom'. This can be inferred from country code e.g. 'GB' or 'UK'",
                },
                "admin1": {
                    "type": "string",
                    "description": "name of administration level 1 Eg 'England'. This can be inferred from admin2 e.g. 'West Midlands' OR can be inferred from admin3 e.g. 'Birmingham' OR can be inferred from country e.g. 'United Kingdom' as 'Birmingham' in 'England' in'United Kingdom'",
                },
                "admin2": {
                    "type": "string",
                    "description": "name of administration level 2 Eg 'West Midlands' This can be inferred from admin3 e.g. 'Birmingham' OR can be inferred from country e.g. 'United Kingdom' as 'Birmingham', in 'West Midlands', in 'United Kingdom'",
                },
                "admin3": {
                    "type": "string",
                    "description": "name of administration level 3 Eg 'Birmingham' This can be inferred from admin2 e.g. 'West Midlands' OR can be inferred from country e.g. 'United Kingdom' as 'Birmingham', in 'West Midlands', in 'United Kingdom'",
                },
            },
        },
    },
    {
        "name": "get_current_weather",
        "description": "Get the current weather for a latitude and longitude.",
        "parameters": {
            "type": "object",
            "properties": {
                "latitude": {
                    "type": "number",
                    "description": "The latitude of the location to get the weather for. Eg 51.56246",
                },
                "longitude": {
                    "type": "number",
                    "description": "The longitude of the location to get the weather for. Eg -0.07401",
                },
            },
        },
    },
]

user_query = "What's the weather like in Dalston, Hackney, London UK?"

response = openai.ChatCompletion.create(
    model="gpt-4-0613",

    # This is the chat message from the user
    messages=[{"role": "user", "content": user_query}],

    functions=function_descriptions,
    function_call="auto",
)
print(f"response {response}")
ai_response_message = response["choices"][0]["message"]


def make_location_dict():
    keys = ["name", "country", "admin3", "admin2", "admin1"]
    args = eval(ai_response_message['function_call']['arguments'])
    return {key: args.get(key, None) for key in keys}


location_details_dict = make_location_dict()

latitude_longitude_json = get_latitude_longitude(location_details_dict['name'])

most_matching_result = find_most_matching_dict(location_details_dict, latitude_longitude_json['results'])

print(f"latitude_longitude_json {latitude_longitude_json}")
print(f"most_matching_result {most_matching_result}")
# latitude = latitude_longitude_json['results'][0]['latitude']
# longitude = latitude_longitude_json['results'][0]['longitude']
#
# user_query = f"What's the weather like at lattitude {latitude} and longitude {longitude}?"
# response = openai.ChatCompletion.create(
#     model="gpt-4-0613",
#
#     # This is the chat message from the user
#     messages=[{"role": "user", "content": user_query}],
#
#     functions=function_descriptions,
#     function_call="auto",
# )
# print(f"response {response}")
# ai_response_message = response["choices"][0]["message"]
# latitude_num = eval(ai_response_message['function_call']['arguments']).get("latitude")
# longitude_num = eval(ai_response_message['function_call']['arguments']).get("longitude")
