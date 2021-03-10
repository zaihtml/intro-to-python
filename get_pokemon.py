import requests

from pprint import pprint

pokemon_number = input("What is the ID of the Pokemon? ")

url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)

response = requests.get(url)

pokemon = response.json()

moves = pokemon['moves']

for height in pokemon:
    print(pokemon['height'])
    print(pokemon['weight'])

for i in pokemon:
    print(i['move']['name'])

