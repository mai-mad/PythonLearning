from turtle import *
from random import *
def sq(a):
    for i in range(4):
        fd(a)
        lt(90)

# sq(100)

n=300#!!! #200 #600
speed(0)
goto(-200, -200)
for i in range(100):
     #        0      1       2
    colors=["blue","black","white"]
    color(colors[i % 3])  # 0..9, 0%3=0, 1%3=1, 2%3=2, 3%3=0, 4%3=1, 5%3=2, 6%3=0
    begin_fill()
    sq(n)
    lt(90)
    up()
    fd(1.5)
    rt(90)
    fd(1.5)
    n = n - 3
    down()
    end_fill()

exitonclick()



