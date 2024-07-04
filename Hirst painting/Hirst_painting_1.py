import colorgram
#get the list of colors from the painting
# def extract_colors(colors):
#     list1 =[]
#     # Getting each index in the list
#     for num in range(len(colors)):
#         each = colors[num]
#         # getting the rgb color in the list
#         pre = each.rgb
#         # getting each colors, r,g,b
#         r = pre.r
#         g = pre.g
#         b = pre.b
#         tuple1 = (r,g,b) #convert them to a tuple
#         list1.append(tuple1) #append the tuple to a list
#     return list1

# list_colors = []
# colors = colorgram.extract('Hirst_art.jpeg',30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     tuple_colors = (r,g,b)
#     list_colors.append(tuple_colors)
# print(list_colors)
# # a = extract_colors(colors)
# # print(a)

import random

def random_colors(color):
    '''returns a random color from list of rgb colors'''
    new_color=random.choice(color)
    return new_color

def go_back():
    for f in range(5):
        t.penup()
        t.forward(50)
        t.pendown()
import turtle as t
#~ Changing the color mode
t.colormode(255)
tim = t.Turtle() #creating a turtle object
list_of_colors = [ (200, 10, 35), (247, 236, 37), (239, 231, 3), (36, 216, 77),
                (223, 159, 61), (39, 79, 185), (28, 39, 159), (210, 73, 16), (17, 151, 18),
                (239, 39, 152), (65, 9, 27), (188, 14, 9), (216, 25, 127), (218, 140, 198), (223, 161, 7),
                (59, 12, 7), (67, 202, 227), (10, 96, 60), (84, 80, 212), (17, 19, 52), (237, 157, 218),
                (106, 232, 195), (99, 205, 136), (212, 84, 58), (8, 222, 235), (236, 171, 161)]

tim.speed('fastest')   #set the turtle speed to fastest
tim.hideturtle()    #hide the turtle
tim.penup()     #lift the pen up while drawing
tim.setheading(225)   #set the turtle direction to 255 degree sp
tim.forward(300)    #turtle moves forward by 300
tim.setheading(360)  #set heading back to 0 degrees or 360 degrees
movement = 100   #number of times the turtle will move

for drawing in range(1,101):    #for loop to execute the drawing
    tim.dot(20,random_colors(list_of_colors))   #tim draws a dot
    tim.forward(50)     #moves forward
    if drawing % 10 == 0:   #if the number divided by 10 the remainder is zero
        #tim to start a new line drawing, go up and draw from beginning
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(360)




my_screen = t.Screen()
my_screen.exitonclick()

