import requests
def recipe_search(ingredient):
    app_id = '82ed5f42'
    app_key = 'fe532c24948af9b8aaae05b633697322'
    result = requests.get ('https://api.edamam.com/api/recipes/v2?type=public&q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))
    data = result.json()
    return data['hits']

def run():
    ingredient = input('Please type your chosen ingredient: ')
    Health = input('Do you have any dietary requirements: Vegetarian, Peanut-Free etc? Or type None if not applicable ')
    List = input('Would you like to save these recipes and their ingredients in a text file? y/n: ')

    results = recipe_search(ingredient)

    for result in results:
        recipe = result['recipe']
        if List == "Y" or List == "y":
            if Health in list(recipe['healthLabels']):
                with open('RecipeList.txt', 'a') as File:
                    File.write(recipe['label'])
                    File.write(': ')
                    File.write(recipe['url'])
                    File.write('\n')
                    File.write("Ingredients: ")
                    File.write(str(recipe['ingredientLines']))
                    File.write('\n')
                    File.write('----------')
                    File.write('\n')
                    print(recipe['label'])
                    print(recipe['url'])
            elif len(Health) == 0 or Health == "None":
                with open('RecipeList.txt', 'a') as File:
                    File.write(recipe['label'])
                    File.write(': ')
                    File.write(recipe['url'])
                    File.write('\n')
                    File.write("Ingredients: ")
                    File.write(str(recipe['ingredientLines']))
                    File.write('\n')
                    File.write('----------')
                    File.write('\n')
                    print(recipe['label'])
                    print(recipe['url'])

        else:
            print(recipe['label'])
            print(recipe['url'])

    if List == 'N' or List == 'n':
        print('-------------')
        print('Your results have not been saved.')

run()

print('-------------')
search_again = input('Would you like to make another search? Y/N: ')

if search_again == 'Y' or search_again == 'y':
    run()

else:
    print('Enjoy your meal :)')