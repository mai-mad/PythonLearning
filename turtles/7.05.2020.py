from turtle import *
from random import *
# circle(150)
n=200
speed(0)
for i in range(67):
    circle(n)
    up()
    n= n-3
    left(90)
    fd(3)
    rt(90)
    down()
hideturtle()
exitonclick()
