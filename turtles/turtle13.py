from turtle import *
from random import *
def fcr(r):
    fillcolor(random(), random(), random())
    begin_fill()
    circle(r)
    end_fill()

window = Screen()

r=200
speed(10)

for i in range(10):
    fcr(r)
    up()
    left(90)
    forward(20)
    r=r-20
    right(90)
    down()



#end figure
exitonclick()