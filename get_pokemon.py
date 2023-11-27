
import requests
from pprint import pprint

pokemon_number = input("What is the Pokemon's ID? ")

url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'

response = requests.get(url)

pokemon = response.json()
height = pokemon['height']
weight = pokemon['weight']
pprint(height)
pprint(weight)      #This section of code is correct

# print(pokemon.keys())
#

# abilities = pokemon['abilities']
#
# pprint(abilities)