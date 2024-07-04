from turtle import Turtle,Screen
import random
#Draw shapes
tim = Turtle()
tim.shape('turtle')
shapes =[3,4,5,6,7,8,9,10] #shapes to be drawn
colors = ['red','blue','black','yellow','orange','pink','purple','green','gray','violet']
for shape in shapes: #looping through eachshapes
    angle = 360/shape
    tim.color(random.choice(colors))
    for drawing in range(shape):
        tim.forward(100)
        tim.right(angle)


my_screen = Screen()
my_screen.exitonclick()

