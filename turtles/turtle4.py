from turtle import *
from random import *


r=200

window = Screen()
shape("turtle")
bgcolor("#000000")
pencolor("red")
speed(0)
pensize(2)

for i in range(360):
    #color("#00ff00") # RGB (red green blue) (00..ff 00..ff 00..ff)

    #random color
    color(random(),random(),random())

    circle(r)
    left(1)

exitonclick()
