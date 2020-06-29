from turtle import *
from random import *


r=0

window = Screen()
shape("turtle")
bgcolor("#000000")
pencolor("red")
speed(15)
pensize(2)

for i in range(36):
    color(random(),random(),random())

    circle(r)
    r=r+10
    left(10)


exitonclick()
