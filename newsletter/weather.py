from NotiWeather import settings
from newsletter.models import User
from urllib import request
import re
import json


API_KEY = settings.WUNDERGROUND_KEY

API_URL = "http://api.wunderground.com/api/{}/conditions/almanac/q/{}/{}.json"

def get_safe_city(city):
    """
    Function that removes periods '.' and replaces whitespace ' ' with
    underscores. The generated url-safe city code will be used to in
    Wunderground API calls.
    """
    no_periods = re.sub('\.', '', city)
    rv_code = re.sub('\s', '_', no_periods)
    return rv_code

def gen_api_url(user):
    """
    Function that generates the URL to be used with Wunderground's REST API
    based on the provide user's location object.
    """
    state = user.location.state_short
    city = get_safe_city(user.location.city)
    return API_URL.format(API_KEY, state, city)

def get_weather_json(user):
    """
    Returns weather information in JSON format for the given user.
    """
    res = request.urlopen(gen_api_url(user))
    data = json.loads(res.read().decode('utf-8'))
    return data