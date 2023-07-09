from src.Request import RequestCall

def get_individual_pokemon(pokemon_name):
    requestCall = RequestCall()
    response = requestCall.get_pokemon(pokemon_name)

    pokemon_information = {
        'id': response['id'],
        'name': response['name'],
        'height': response['height'],
        'weight': response['weight'],
        'sprites': response['sprites']['front_default']
    }
    print(pokemon_information)
    return pokemon_information