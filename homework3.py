# Create a program that tells you whether or not you need an umbrella when you leave the house

weather = input("Is it raining? y/n ")

if weather == 'y':
    print("Take an umbrella.")
else:
    print("You don't need an umbrella.")

# work out the problem in this code

my_money = input('How much money do you have? ')
boat_cost = 20 + 5

if my_money > boat_cost:
    print('You can afford the boat hire.')
else:
    print('You cannot afford the boat hire.')

# write a program that takes a year and outputs the century and decade

book_year = int(input("What year was the book written? "))

if book_year >= 1950:
    print("Late twentieth century")
elif book_year >= 1940:
    print("Twentieth century, Forties")
elif book_year >= 1930:
    print("Twentieth century, Thirties")
elif book_year >= 1920:
    print("Twentieth century, Twenties")
elif book_year >= 1910:
    print("Twentieth century, Tens")
elif book_year >= 1900:
    print("Twentieth century, Noughties")
elif book_year >= 1890:
    print("Nineteenth century, Nineties")
elif book_year >= 1880:
    print("Nineteenth century, Eighties")
elif book_year >= 1870:
    print("Nineteenth century, Seventies")
elif book_year >= 1860:
    print("Nineteenth century, Sixties")
elif book_year >= 1850:
    print("Nineteenth century, Fifties")
elif book_year >= 1840:
    print("Nineteenth century, Forties")
elif book_year >= 1830:
    print("Nineteenth century, Thirties")
elif book_year >= 1820:
    print("Nineteenth century, Twenties")
elif book_year >= 1810:
    print("Nineteenth century, Tens")
elif book_year >= 1800:
    print("Nineteenth century, Noughties")
else:
    print("Pre-nineteenth century")