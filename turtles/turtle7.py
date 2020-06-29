from turtle import *
from random import *


r=100

window = Screen()
shape("turtle")
bgcolor("#000000")
pencolor("red")
speed(4)
pensize(2)

for i in range(4):
    color(random(),random(),random())

    circle(r, 90)
    #r=r+10
    #left(10)


exitonclick()
