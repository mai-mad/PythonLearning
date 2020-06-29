from turtle import *
from random import *

def tr(a):
    for i in range(3):
        fd(a)
        rt(120)


def umbrella(a):
    for i in range(6):
        color(random(), random(), random())
        begin_fill()
        rt(60)
        if i%2==0: # 0%2=0, 1%2=1, 2%2=0, 3%2=1
            tr(a)
        else:
            tr(a*2)
        end_fill()

speed(9)

umbrella(100)

exitonclick()