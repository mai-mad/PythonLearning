from turtle import *
from random import *
def fcr(r):
    fillcolor(random(), random(), random())
    begin_fill()
    circle(r)
    end_fill()

window = Screen()

r=180
speed(0)

for k in range(18):
    for i in range(4):
        fcr(r)
        up()
        left(90)
        forward(20)
        down()
    r=r-10
    left(12)



#end figure
exitonclick()