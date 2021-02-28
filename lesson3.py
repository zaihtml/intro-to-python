# An example if/else statement to check if the price of a burger is within a budget.
price = input("What is the price of the burger?")

is_affordable = float(price) <= 10.0

print('The burger is within my budget: {}'.format(is_affordable))

# adding to the above code to input whether the restaurant has a vegetarian option

veg = input("Does the restaurant have a vegetarian option? y/n ")

has_veg = veg == "y"

should_visit_restaurant = is_affordable and has_veg
print('Restaurant meets criteria. {}'.format(should_visit_restaurant))

# rewrite the output of your burger program to use if statements

if should_visit_restaurant:
    print('This restaurant is a great choice!')

else:
    print('Probably not a good idea')

# write a program to calculate your meal and apply a discount if applicable

meal_price = float(input('How much did the meal cost?'))

discount_choice = input('Do you have a discount? y/n ')
discount_applicable = discount_choice == 'y'

new_price = meal_price - (meal_price / 10)

if meal_price >= float(20.0):
    print('Discount applied. New price is {}'.format(new_price))

else:
    print('No discount')

# you're cooking a pizza and need to check that the oven is at the right temperature

temperature = int(input('What is the oven temperature?'))

if temperature > 200:
    print('The oven is too hot')

elif temperature < 150:
    print('The oven is too cold')

elif temperature == 180:
    print('The oven is at the perfect temperature')

else:
    print('The temperature is close enough')
