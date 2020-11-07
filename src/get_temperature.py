"""
get_temperature.py

Return the temperature of Montreal at a given time. Future versions: take city name as input and return temperature of that city.

"""

import requests
import json
import os.path as osp

def get_temperature():

    # Montreal city code is: 6077243
    montreal = 6077243
    api_key = "1c7b67b1e9de33125b6801dc38c28efc"

    data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?id={montreal}&appid={api_key}&units=metric')
    contents = data.json()
    temperature = contents['main']['temp']

    return temperature

# this is how I would get the city name, in future. They have multiple entries for the same cities, would need country code from dropdown too
"""
def get_city(city_name):

    cities = osp.join(osp.dirname, '..', 'data', city_list.json)
    list(filter(lambda city: city['name'] == 'Montréal', cities))
"""
