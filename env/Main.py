import json

from flask import Flask, request
from flask_cors import CORS
from src.get_pokedex_list import get_pokedex_list

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return '<p>Hello</p>'

@app.route('/pokedex/<limit>', methods=['GET'])

def get_limit(limit):
    try: 
        print('getting api')
        list = get_pokedex_list(limit)
        response= app.response_class (
            response= json.dumps(list),
            status=200,
            mimetype='application/json'
        )
    except(Exception) as error:
        response = app.response_class(
            response=f'error has occurred: {error}',
            status=400,
            mimetype='application/json'
        )
    return response