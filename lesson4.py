# exercise 4.1

winter_clothes = [
    'shorts',
    'gloves',
    'hat',
    'boots',
]

print(winter_clothes)

if winter_clothes[0] == 'shorts':
    winter_clothes[0] = 'warm coat'

print(winter_clothes)

# exercise 4.2

game_scores = [ 2, 4, 6, 8, 10, 12, 14, 16, 18, 20 ]

print(len(game_scores))

print(max(game_scores))

print(min(game_scores))

print(sorted(game_scores))

print(list(reversed(game_scores)))

# exercise 4.3

shopping_list = [
    'grapes', 'cheese', 'oil', 'waffles'
]

if 'bread' in shopping_list:
    print('{} is in the shopping list'.format('bread'))
    shopping_list.append('butter')
else:
    print('{} is not in the shopping list'.format('bread'))


print(shopping_list)

# exercise 4.4

costs = [8.30, 7.12, 5.01, 1.00, 0.99, 5.92, 3.50]
total_cost = 0

for i in costs:
    total_cost = sum(costs)

print(total_cost)

# exercise 4.5

place = {
'name': 'The Anchor',
'post_code': 'E14 6HY',
'street_number': '54',
'location': {
'longitude': 127,
'latitude': 63,
}
}

print(place['name'], place['post_code'], place['street_number'])
print(place['post_code'])
print(place['street_number'])
# extension
print(place['location'])

# exercise 4.6

fruits = [
{'name': 'apple', 'colour': 'red', 'price': 0.12},
{'name': 'banana', 'colour': 'yellow', 'price': 0.2},
{'name': 'pear', 'colour': 'green', 'price': 0.19},
]

for fruit in fruits:
    print(fruit['name'])
    print(fruit['colour'])
    print(fruit['price'])

# exercise 4.7

import random

names = ['Nick', 'Jess', 'Winston', 'Cece', 'Schmidt', 'Coach']
chosen_name = random.choice(names)

print(chosen_name)

# extension

nouns = ['penguin ', 'red ', 'spoon ', 'shoe ']
verbs = ['run', 'swim', 'eat', 'lift']

print("The loud " + random.choice(nouns) + "is going to " + random.choice(verbs))