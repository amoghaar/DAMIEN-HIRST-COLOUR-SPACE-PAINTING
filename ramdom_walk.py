from turtle import Turtle, Screen
from random import choice, randint

colors = ["Black", "Black", "DarkGreen", "Black", "Black", "Black", "Black", "Indigo", "DarkSlateGray", "Green",
          "MidnightBlue", "DarkCyan", "DarkOrange", "DarkOrchid", "DarkOliveGreen", "DarkSlateBlue", "DarkViolet",
          "MediumVioletRed", "MediumBlue", "DarkBlue", "DarkGreen", "Fuchsia", "DarkGoldenrod", "OliveDrab",
          "DarkOrange", "Firebrick"]

move = ["forward", "backward", "right", "left"]

ammu = Turtle()
ammu.shape("turtle")
ammu.color("green")
ammu.pensize(15)
ammu.speed("fast")

random_move = 300
angle = 90

for i in range(random_move):
    ammu.color(choice(colors))
    distance = randint(1, 50)
    decided_move = choice(move)
    if decided_move == "forward":
        ammu.forward(distance)
    elif decided_move == "backward":
        ammu.backward(distance)
    elif decided_move == "right":
        ammu.right(angle)
    elif decided_move == "left":
        ammu.left(angle)

screen = Screen()
screen.exitonclick()