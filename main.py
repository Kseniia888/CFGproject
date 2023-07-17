import pprint
import requests
import json
import sys

sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

ingredient = input('What ingredient should be in recipes? ')


def recipe_search(ingredient):
    # Register to get an APP ID and key: https://developer.edamam.com/
    app_id = 'a2a43e33'
    app_key = '7230c73e5b23cf4676d66b140694077c'
    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)
    result = requests.get(url)
    data = result.json()
    return data['hits']


# First extension
def save_result():
    results = recipe_search(ingredient)
    with open('saved_res.txt', 'w', encoding='utf-8') as file:
        for result in results:
            recipe = result['recipe']
            file.write(recipe['label'] + "\n")
            file.write(recipe['shareAs'] + "\n")
            file.write("\n")
    print("Data saved to 'saved_res.txt' file.")


save_result()


def run():
    results = recipe_search(ingredient)
    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['shareAs'])
        print()


run()

# Helper function to create and write JSON file
def create_and_write_json_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file)
    print(f"Data written to '{filename}' file.")


# Save recipe data to JSON file
data_from_data = recipe_search(ingredient)
create_and_write_json_file(data_from_data, 'data.json')

# Second extension
# Sort recipes by total weight and save to a new JSON file
data_from_data1 = sorted(data_from_data, key=lambda x: x['recipe']['totalWeight'], reverse=True)
create_and_write_json_file(data_from_data1, 'sortedData.json')

pprint.pprint(data_from_data)

# Third extention

def choose_a_dish():
    kcals = input('Approximately how much kcal must be in dish (type max amount) ')
    results = recipe_search(ingredient)
    found_dish = False
    for result in results:
        recipe = result['recipe']
        if recipe['totalNutrients']['ENERC_KCAL']['quantity']<= float(kcals):
            found_dish = True
            print('That dish below is perfect choice ')
            print(recipe['label'])
            print(recipe['shareAs'])
            break
    if not found_dish:
             print('Sorry, no dish found according to your parameters, please change your search parameters ')
choose_a_dish()