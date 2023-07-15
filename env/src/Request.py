import os
from dotenv import load_dotenv, find_dotenv
import requests

class RequestCall:

    def __init__(self) -> None:
        load_dotenv(find_dotenv())
        self.offset = '&offset=0'
        self.base_url = os.getenv('POKEDEX_BASE_API')
        self.limit_url = os.getenv('POKEDEX_LIMIT_API')
        self.individual_url = os.getenv('INDIVIDUAL_POKEMON_API')

    def get_pokemon_list(self, limit):
        try:
            response = requests.get(self.limit_url + limit + self.offset)

            data = response.json()
            list_of_result = data['results']

            # will create a new list with each pokemons information
            result = [(self.get_pokemon(pokemon['name'])) for pokemon in list_of_result]

            return result
        except(Exception) as error:
            return error
    
    def get_pokemon(self,pokemon_name):
        try:
            response = requests.get(self.individual_url + pokemon_name)

            data = response.json()
            # print(data['types'][0]['type'])
            
            pokemon_types = [(types['type']['name']) for types in data['types']]

            # will map useful information from api into a new object that can be used in front end
            pokemon_information = {
            'id': data['id'],
            'name': data['name'],
            'height': data['height'],
            'weight': data['weight'],
            'sprites': data['sprites']['front_default'],
            'types': pokemon_types
            }

            return pokemon_information
        except(Exception) as error:
            return error