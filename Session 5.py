#Writing to a file

# with open('people.txt', 'w+') as text_file:
#     people = 'Joanne \nSusan \nAmina'
#
#     text_file.write(people)
#
# #Reading from a file
#
# with open('people.txt', 'r') as text_file:
#     contents = text_file.readlines()
#
# print(contents)
# print(type(contents))

# with open('todo.txt' , 'r') as text_file:
#     contents = text_file.readlines()
#     new_job = input("What job would you like to add? ")
#
# new_todo = input("What do you want to add to the to do list?")
#
# with open('todo.txt', 'w+') as text_file:
#     text_file.write(new_todo)


# import csv     *****GO OVR THIS!!******
#
# with open('trees.csv', 'r') as csv_file:
#
#     spreadsheet = csv.DictReader(csv_file)
#
#     heights = []  # this is an empty list because it will create it in the for loop below
#
#     for row in spreadsheet:
#         tree_height = row['height']   #this runs each row and pulls the height value
#         heights.append(tree_height)   #this then appends the list
#
# shortest_height = min(heights)
# print(shortest_height)
# *********************************

#homework

# poem = 'I like Python and I am not very good at poems'
# with open('poem.txt', 'r') as poem_file:     #for the code to work you need to change the r to w for write because the poem.txt file doesnt exist yet
#     poem_file.write(poem)



#In this session you used the Pokemon API to retrieve a single Pokemon. I want a program that can
#retrieve multiple Pokemon and save their names and moves to a file.
#Use a list to store about 6 Pokemon IDs. Then in a for loop call the API to retrieve the data for each
#Pokemon. Save their names and moves into a file called 'pokemon.txt'

import requests
pokemon_number = [6, 8, 2, 10, 12, 15]

with open('pokemon.txt', 'w') as file:
    for pokemon in pokemon_number:
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}/'

        response = requests.get(url)


        pokemon_data = response.json()

        pokemon_name = pokemon_data['name']
        pokemon_moves = pokemon_data['moves']

        file.write(f"Name: {pokemon_name}\n")

        for move in pokemon_data['moves']:
            move_name = move['move']['name']
            file.write(f"- {move_name}\n")










