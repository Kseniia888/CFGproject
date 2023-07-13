import pprint
import requests
import json

ingredient = input('What ingredient should be in recipes? ')

def recipe_search(ingredient):
    # Register to get an APP ID and key https://developer.edamam.com/
    app_id = 'a2a43e33'
    app_key = '7230c73e5b23cf4676d66b140694077c'
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)
    )
    data = result.json()
    return data['hits']

def run():
    results = recipe_search(ingredient)

    for result in results:
        recipe = result['recipe']


        print(recipe['label'])
        print(recipe['shareAs'])
        print()


run()

def create_and_write_json_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)
    print(f"Data written to '{filename}' file.")

data_from_data = recipe_search(ingredient)
create_and_write_json_file(data_from_data, 'data.json')

data_from_data = sorted(data_from_data, key=lambda x: x['recipe']['totalWeight'], reverse=True)
pprint.pprint(data_from_data)
