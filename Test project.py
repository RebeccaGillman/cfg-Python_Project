import requests
def recipe_search(ingredient):
    app_id = '0156b69f'
    app_key = '9f1aefffe0adc9163731615352b03292'
    result = requests.get ('https://api.edamam.com/api/recipes/v2?type=public&q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    #print (data)
    return data['hits']


def health_preference(ingredient, Health):
    results = recipe_search(ingredient)
    matching_results = []
    with open('recipe_results.txt', 'w') as file:
       for result in results:
          recipe = result['recipe']
          if Health in list(recipe['healthLabels']):
            file.write(f"'Label: {recipe['label']},\n'")
            file.write(f"'URL: {recipe['url']},\n'")
            file.write('\n')
            print(recipe['label'])
            print(recipe['url'])


    return matching_results


def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)
    Health = input('Do you have any of the following dietary requirements: Vegetarian, Peanut-Free?, None  ')
    if Health == 'None':
       with open('recipe_results.txt', 'w') as file:
           for result in results:
               recipe = result['recipe']
               file.write(f"'Label: {recipe['label']},\n'")
               file.write(f"'URL: {recipe['url']},\n'")
               file.write('\n')

               print(recipe['label'])
               print(recipe['url'])


    elif Health == 'Vegetarian' or Health == 'Peanut-Free':
       matching_results = health_preference(ingredient, Health)


run()


# def save_results_to_file(results, filename):
#     with open(filename, 'w') as file:
#         for result in results:
#             recipe = result['recipe']
#             file.write(f"'Label: {recipe['label']},\n'")
#             file.write(f"'URL: {recipe['url']},\n'")
#             file.write('\n')