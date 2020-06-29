from turtle import *
from random import *

# rectangle function
def rect(color):
    fillcolor(color)
    begin_fill()
    fd(200)
    right(90)
    fd(50)
    right(90)
    fd(200)
    right(90)
    fd(50)
    right(90)
    end_fill()

window = Screen()
bgcolor("grey")


rect("white")
rt(90)
fd(50)
lt(90)
rect("blue")
rt(90)
fd(50)
lt(90)
rect("red")

exitonclick()