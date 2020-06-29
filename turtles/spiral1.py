from turtle import *
from random import *

# draw spiral
def spiral(a):
    x = 1
    for i in range(a):
        color(random(),random(),random())
        fd(x)
        x = x +3
        rt(90)

def spiral2(a):
    x = 5

    for i in range(a):
        color(random(),random(),random())
        #fillcolor(random(),random(),random())
        #begin_fill()
        fd(x)
        #end_fill()
        x = x + 1
        rt(30)


window = Screen()

speed(0)

spiral2(200)
#spiral(350)



exitonclick()