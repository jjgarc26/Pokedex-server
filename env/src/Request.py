import os
from dotenv import load_dotenv, find_dotenv
import requests

class RequestCall:

    def __init__(self) -> None:
        print('init')
        load_dotenv(find_dotenv())
        self.base_url = os.getenv('POKEDEX_BASE_API')
        self.limit_url = os.getenv('POKEDEX_LIMIT_API')
        self.individual_url = os.getenv('INDIVIDUAL_POKEMON_API')

    def get_pokemon_list(self, limit):
        offset = '&offset=0'
        response = requests.get(self.limit_url + limit + offset)
        return response.json()
    
    def get_pokemon(self,pokemon_name):
        response = requests.get(self.individual_url + pokemon_name)
        return response.json()