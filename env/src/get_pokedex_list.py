
import os
from dotenv import load_dotenv, find_dotenv
import requests

def get_pokedex_list(limit):
    try:
        load_dotenv(find_dotenv())

        base_url = os.getenv('POKEDEX_BASE_API')
        limit_url = os.getenv('POKEDEX_LIMIT_API')

        response_result = requests.get(base_url + limit_url + limit + '&offset=0')
        return response_result.json()
    except(Exception) as error:
        response = error
    return response