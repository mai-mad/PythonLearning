from turtle import *
from random import *
def fcr(r):
    fillcolor(random(), random(), random())
    begin_fill()
    circle(r)
    end_fill()


r=10
s=100

window = Screen()
shape("turtle")
bgcolor("#000000")
pencolor("red")
speed(50)
pensize(2)

for i in range(36):
    fcr(r)
    left(10)
    s = s + 10
    r= r+10
exitonclick()

