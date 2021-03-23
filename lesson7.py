# team working session
# recipe search project
# this is the basic search function where the user is asked what ingredient they are searching for
# then the function makes a request to the API with the ingredient as part of the search query
# the results are then returned from the API

import requests

from pprint import pprint

ingredient = input('What ingredient are you looking for? ')

url = 'https://api.edamam.com/search?q=aubergine&app_id=ac163df5&app_key=a304cf9b2a79c2dbf8ccfb1ec3aef68e&from0&to1'.format(ingredient)

response = requests.get(url)
results = response.json()

pprint(results)

# I am having trouble displaying the recipes only

