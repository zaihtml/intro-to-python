

"""# create a text file
with open('me.txt', 'w') as my_file:
    bio = 'My name is Zainab.'

    my_file.write(bio)

with open('me.txt', 'r') as my_file:
    contents = my_file.read()

print(contents)

# exercise 5.1

# ask the user to input a new to-do item
new_task = input('What is your next task?')

# read the contents of the existing to-do items
with open('todo.txt', 'r') as todo_file:
    task = todo_file.read()

# add the new item to the existing to-do items
task = task + new_task + '\n'

# save the updated to-do items
with open('todo.txt', 'w') as todo_file:
    todo_file.write(task)

# writing a CSV (comma-separated value)

import csv

field_names = ['name', 'age']

data = [
    {'name': 'Jill', 'age': 32},
    {'name': 'Sara', 'age': 28},
]

with open('team.csv', 'w+') as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)

    spreadsheet.writeheader()
    spreadsheet.writerows(data)

# reading a csv

with open('team.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)
    for row in spreadsheet:
        print(dict(row))
"""
# exercise 5.2, read data about trees from a file to find the shortest file

import csv

with open('trees.csv', 'r') as my_trees:
    spreadsheet = csv.DictReader(my_trees)

    heights = []

    for row in spreadsheet:
        tree_height = row['height']
        heights.append(tree_height)

shortest_height = min(heights)
print(shortest_height)
