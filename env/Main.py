import json

from flask import Flask, request
from flask_cors import CORS
from src.Request import RequestCall

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return '<p>Hello</p>'

@app.route('/pokedex/<limit>', methods=['GET'])

def get_limit(limit):
    try: 
        print('Getting list of pokemons')
        request = RequestCall()
        data = request.get_pokemon_list(limit)
        response= app.response_class (
            response= json.dumps(data),
            status=200,
            mimetype='application/json'
        )
    except(Exception) as error:
        response = app.response_class(
            response=f'error has occurred in "pokedex/{limit}": {error}',
            status=400,
            mimetype='application/json'
        )
    return response

@app.route('/pokemon/<pokemon_name>', methods=['GET'])

def get_pokemon(pokemon_name):
    try:
        print('Getting pokemon information')
        request = RequestCall()
        data = request.get_pokemon(pokemon_name)
        response = app.response_class(
            response = json.dumps(data),
            status = 200,
            mimetype = 'application/json'
        )
    except(Exception) as error:
        response = app.response_class(
            response=f'error has occurred in "pokedex/{pokemon_name}": {error}',
            status=400,
            mimetype='application/json'
        )
    return response