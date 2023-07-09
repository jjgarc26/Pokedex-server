
import os
from dotenv import load_dotenv, find_dotenv
import requests
from src.Request import RequestCall

def get_pokedex_list(limit):
    try:
        request_call = RequestCall()
        response = request_call.get_pokemon_list(limit)
        
        return response
    except(Exception) as error:
        response = error
    return response