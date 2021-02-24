"""question 2
my_name = "Penelope"
my_age = 29

message = 'My name is {} and I am {} years old.'.format(my_name, my_age)
print(message)"""

"""I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can make.
Write a program to calculate this.
Assume that a box of eggs contains six eggs and I need four eggs for each omelette, but I should be
able to easily change these values if I want. The output should say something like "You can make 9
omelettes with 6 boxes of eggs"."""

"""total_boxes = 12
eggs_for_omelette = 4
eggs_in_box = 6

total_eggs = eggs_in_box * total_boxes
omelettes = total_eggs / eggs_for_omelette

output = 'You can make {} omelettes with {} boxes of eggs.'.format(omelettes, total_boxes)
print(output)"""

def omelettes():
    total_boxes = 12
    eggs_for_omelette = 4
    eggs_in_box = 6

    total_eggs = eggs_in_box * total_boxes
    omelettes = total_eggs / eggs_for_omelette

    output = 'You can make {} omelettes with {} boxes of eggs.'.format(omelettes, total_boxes)
    print(output)

omelettes()
