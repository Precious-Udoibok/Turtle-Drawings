#random walk
import turtle as t
import random

#random walk
def random_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tuple1 = (r,g,b)
    return tuple1
t.colormode(255)
tim = t.Turtle()
angle = [0,90,180,270]
tim.speed('fastest')
tim.pensize(10)
for _ in range(200):
    tim.forward(40)
    #set the heading of the turtle to a random degree from the list
    tim.setheading(random.choice(angle))
    tim.color(random_colors())

my_screen = t.Screen()
my_screen.exitonclick()