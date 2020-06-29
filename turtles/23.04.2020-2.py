from turtle import *
from random import *

def tr(a):
    for i in range(3):
        fd(a)
        rt(120)



for i in range(6):
    color(random(), random(), random())
    begin_fill()
    rt(60)
    tr(100)
    end_fill()



exitonclick()