# basic till program to check the price of chocolates

chocolate = {
    'white': 1.50,
    'milk': 1.20,
    'dark': 1.80,
    'vegan': 2.00,
}
customer_choice = input('Which chocolate do you want?')

if customer_choice == 'white':
    print(chocolate['white'])
elif customer_choice == 'milk':
    print(chocolate['milk'])
elif customer_choice == 'dark':
    print(chocolate['dark'])
elif customer_choice == 'vegan':
    print(chocolate['vegan'])
else:
    print('Enter valid choice.')

# lottery ticket program

from random import randint
lottery_ticket = {
    12, 56, 38, 50, 27, 30, 94,
}
for numbers in range(7):
    winning_nums = randint(0, 99)
    print(winning_nums)

if winning_nums == lottery_ticket:
    print('You have won £1,000,000!')
elif 