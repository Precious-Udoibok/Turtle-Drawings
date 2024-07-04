import turtle as t
import random
# Draw a Siprograph.
def random_colors():
    '''Returns a tuple of random rgb colors'''
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tuple1 = (r,g,b)
    return tuple1

#changing the turtle's colormode
t.colormode(255)
tim = t.Turtle()
tim.speed('fastest')
for angle in range(0,370,2):
    tim.color(random_colors())
    #tilt the angle
    tim.setheading(angle)
    tim.circle(100) #draws a circle





my_screen = t.Screen()
my_screen.exitonclick()