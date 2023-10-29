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
        self.kanto_pokedex = os.getenv('KANTO_POKEDEX')
        self.johto_pokedex = os.getenv('JOHTO_POKEDEX')
        self.hoenn_pokedex = os.getenv('HOENN_POKEDEX')
        self.sinnoh_pokedex = os.getenv('SINNOH_POKEDEX')


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
        
    def get_region_information(self, region):
        try:
            print('Getting region information')
           
            # sends GET request to retrieve region  pokedex
            region_pokedex = self.get_region_pokedex(region)
            print(region_pokedex)
        
            # response = requests.get(self.base_url + 'region/' + region)
            # data = response.json()
            return region_pokedex
            
        except(Exception) as error:
            return error
        
    def get_region_pokedex(self, region):
        try:
            print(f'Getting {region} region pokedex')

            region_endpoint = self.get_pokedex_region_endpoint(region)
            
            request_url = self.base_url + region_endpoint

            request = requests.get(request_url)
            data = request.json()
            print("POKEMON ENTRIES")

            result = [(self.get_pokemon(pokemon['pokemon_species']['name'])) for pokemon in data['pokemon_entries']]

            return result
        except(Exception) as error:
            return error
        
    def get_pokedex_region_endpoint(self, region):
        try:
            print('Getting region endpoint')
            region_endpoint = {
                "kanto" : self.kanto_pokedex,
                "johto": self.johto_pokedex,
                "hoenn": self.hoenn_pokedex,
                "sinnoh": self.sinnoh_pokedex
            }
            return region_endpoint[region]
        except(Exception) as error:
            print("Could not get enpoint")
            return error
    