""""# exercise 1
name = input("What is your name?")
print("Hello, {}".format(name))

colour = input("What is your favourite colour?")
room_colour = input("Would you paint your room this colour?")

print("You like {} and the answer to whether you\'d paint your room this colour is {}.".format(colour, room_colour))

# exercise 2
friends = int(input("How many are your friends?"))
pizzas = friends * 0.5

print("You need {} pizzas to feed {} friends".format(pizzas, friends))"""

# exercise 4
import turtle
sides = int(input('Number of sides: '))

angle = 360 / sides
side_length = 60

for side in range(3):
    turtle.forward(side_length)
    turtle.right(angle)

    turtle.done()

# exercise 5
import turtle

def triangle():
    angle = -120 # I've set this as minus bc that stops the triangle forming upside down
    side_length = 100

    for side in range(3):
        turtle.forward(side_length)
        turtle.right(angle)

        turtle.done()

triangle()

# exercise 6
import turtle

def blue_triangle(side_length, color):
    angle = -120

    turtle.color(color, color)
    turtle.begin_fill()

    for side in range(3):
        turtle.forward(side_length)
        turtle.right(angle)

    turtle.end_fill()
    turtle.done()

blue_triangle(100, 'red')
blue_triangle(80, 'blue')
blue_triangle(60, 'yellow')
blue_triangle(40, 'green')

# exercise 7
def circle_area(radius):
    area = 3.14 * (radius ** 2)
    return area

area = circle_area(10)

print(area)

