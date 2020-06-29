from turtle import *
from random import *

def star(a):
    colors=["blue","black","white","blue","black"]
    x=1
    for i in range(a):
        color(colors[i%5])
        fd(x)
        x = x + 10
        lt(144)

bgcolor("gray")
speed(0)
star(70)

exitonclick()