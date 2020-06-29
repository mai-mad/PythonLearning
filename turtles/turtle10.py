from turtle import *
from random import *

def tr(a):
    fillcolor(random(), random(), random())
    begin_fill()
    fd(a)
    left(120)
    fd(a)
    left(120)
    fd(a)
    left(120)
    end_fill()

r=360
s=100

window = Screen()
shape("turtle")
bgcolor("#000000")
pencolor("red")
speed(10)
pensize(2)



for i in range(36):
    tr(s)
    left(10)
    s = s + 10
exitonclick()