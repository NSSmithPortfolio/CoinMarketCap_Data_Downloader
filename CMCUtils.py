import json
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects

import os

from os.path import join, dirname
from dotenv import load_dotenv
from pathlib import Path


def pull_CMC_data():
    API_key = get_API_password()

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start': '1',
        'limit': '2000',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': API_key,
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        try:
            CMC_data = json.loads(response.content)  # dataList variable is actually a list of dictionaries.
        except:
            print("No data returned on CMC")

        return CMC_data

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def get_API_password():
    load_dotenv()

    # retrieving keys and adding them to the project
    # from the .env file through their key names
    API_SECRET_KEY = os.getenv("API_KEY")
    # print("key found:", API_SECRET_KEY)

    return API_SECRET_KEY
