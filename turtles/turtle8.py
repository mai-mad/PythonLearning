from turtle import *
from random import *


r=100

window = Screen()
shape("turtle")
bgcolor("#000000")
pencolor("red")
speed(20)
pensize(2)

for i in range(360):
    color(random(),random(),random())
    circle(r, 1)
exitonclick()