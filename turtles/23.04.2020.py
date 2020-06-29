from turtle import *
from random import *

# a - size of the square
def square(a):
    for i in range(4):
        fd(a)
        rt(90)


left(120)

for i in range(24):
    left(15)
    square(100)

exitonclick()