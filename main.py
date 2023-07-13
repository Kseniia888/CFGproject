
import pprint
import requests
import json
import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

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

#First extention 

def save_result ():
    with open('saved_res.txt', 'w') as file:
        results = recipe_search(ingredient)
        for result in results:
            recipe = result['recipe']
            file.write(recipe['label'] + "\n")
            file.write(recipe['shareAs'] + "\n")
            file.write("\n")

save_result()
print("Data saved to 'saved_res.txt' file.")

#second extention

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


def sorting_by_func(data, filename):
    data_from_data = recipe_search(ingredient)

    with open(filename, 'w') as file:
        json.dump(data, file)

data_from_data1 = sorted(data_from_data, key=lambda x: x['recipe']['totalWeight'], reverse=True)
sorting_by_func(data_from_data1, 'sortedData.json')
pprint.pprint(data_from_data)