from turtle import *
from random import *


r=100

window = Screen()
shape("turtle")
bgcolor("#000000")
pencolor("red")
speed(15)
pensize(2)

for i in range(2):
    color(random(),random(),random())

    circle(r, 180)
    #r=r+10
    #left(10)


exitonclick()
