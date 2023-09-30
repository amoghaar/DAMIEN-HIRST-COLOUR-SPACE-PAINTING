from turtle import Turtle, Screen, colormode
from random import randint

ammu = Turtle()
ammu.speed(0)
colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color = (r, g, b)
    return color


def spirograph(gap_size):
    for i in range(int(360 / gap_size)):
        ammu.color(random_color())
        ammu.circle(100)
        ammu.setheading(ammu.heading() + gap_size)

spirograph(5)

screen = Screen()
screen.exitonclick()
