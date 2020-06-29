from turtle import *
from random import *
def fcr(r):
    fillcolor(random(), random(), random())
    begin_fill()
    circle(r)
    end_fill()




window = Screen()

r=100
fcr(r)
left(90)

up()

forward(20)
down()
right(90)
r=80
fcr(r)

left(90)
forward(20)
right(90)
r=60
fcr(r)
exitonclick()
