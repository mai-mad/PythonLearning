from turtle import *
from random import *
def tr(a):
    for i in range(3):
        fd(a)
        lt(120)

n = 200


for i in range(10):
    #        0      1       2
    colors=["blue","black","white"]
    color(colors[i % 3])  # 0..9, 0%3=0, 1%3=1, 2%3=2, 3%3=0, 4%3=1, 5%3=2, 6%3=0
    begin_fill()
    tr(n)
    lt(23)
    up()
    fd(11)
    rt(23)
    n = n - 20
    down()
    end_fill()


exitonclick()



