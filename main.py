
import requests




def recipe_search(ingredient):
# Register to get an APP ID and key https://developer.edamam.com/
    app_id = 'a2a43e33'
    app_key = '7230c73e5b23cf4676d66b140694077c'
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id,
        app_key)
    )
    data = result.json()
    return data['hits']


def run():
    ingredient = input('What ingredient should be in recipes? ')
    results = recipe_search(ingredient)

    for result in results:
        recipe = result['recipe']


        print(recipe['label'])
        print(recipe['shareAs'])
        print()


run()
