"""
get_temperature.py

Return the temperature of Montreal at a given time. Future versions: take city name as input and return temperature of that city.

"""

import requests
import json
import os.path as osp
import argparse
import country_converter

script_dir = osp.dirname(__file__)

def get_temperature(city, country):

    api_key = "1c7b67b1e9de33125b6801dc38c28efc"

    # convert country code to ISO2 standard (required by API)
    country_ISO = country_converter.convert(country, to='ISO2')

    # get city id
    city_id = get_city_id(city, country_ISO)

    # pull temperature, given city_id
    data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?id={city_id}&appid={api_key}&units=metric')
    contents = data.json()
    temperature = contents['main']['temp']

    return temperature

def get_city_id(city, country):

    # pull city listing from data directory
    cities = json.load(open(osp.join(script_dir, '..', 'data', 'city_list.json'), "r"))
    # filter city to listings of that city and country, in case more than 1 just take the first entry
    city_listing = list(filter(lambda entry: entry['name'] == city and entry['country'] == country, cities))[0]

    # return city id
    return city_listing['id']

