# to extract the colour rom the image will use the below commented code
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r, g, b)
#     rgb_colors.append(new_colors)
#
# print(rgb_colors)


import turtle
from turtle import Turtle, Screen
from random import choice

turtle.colormode(255)
ammu = Turtle()
ammu.shape("turtle")
ammu.color("green")
ammu.hideturtle()


def row_print():
    """prints the row"""
    for i in range(10):
        random_color = choice(color_list)
        ammu.dot(20, random_color)
        ammu.penup()
        ammu.forward(50)
        ammu.pendown()


def left_move_next_line():
    """moves to next row printing from left side"""
    row_print()
    ammu.penup()
    ammu.left(90)
    ammu.forward(50)
    ammu.left(90)
    ammu.forward(50)


def right_move_next_line():
    """moves to next row printing from right side"""
    row_print()
    ammu.penup()
    ammu.right(90)
    ammu.forward(50)
    ammu.right(90)
    ammu.forward(50)


color_list = [(195, 12, 34), (42, 80, 177), (237, 40, 138), (32, 40, 156), (21, 150, 23),
    (209, 73, 21), (204, 32, 96), (66, 10, 28), (217, 163, 11), (218, 137, 191),
    (189, 15, 9), (55, 15, 10), (77, 211, 153), (68, 72, 221), (86, 189, 222),
    (14, 94, 64), (237, 158, 213), (99, 234, 198), (20, 20, 51), (216, 87, 52),
    (4, 229, 240), (14, 68, 46)]

# to come to the position to print the painting
ammu.penup()
ammu.right(90)
ammu.forward(200)
ammu.right(90)
ammu.forward(200)
ammu.right(180)

# the printing starts from here
for i in range(5):
    left_move_next_line()
    right_move_next_line()

# come out of the painting
screen = Screen()
screen.exitonclick()