from turtle import *
from random import *


r=360

window = Screen()
shape("turtle")
bgcolor("#000000")
pencolor("red")
speed(20)
pensize(2)

up()
goto(0, -330)
down()

for i in range(360):
    color(random(),random(),random())
    fillcolor(random(),random(),random())
    begin_fill()
    circle(r)
    end_fill()
    r = r - 1
exitonclick()