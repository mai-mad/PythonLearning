from turtle import *
from random import *
# 1task: A

r=150

window = Screen()
shape("turtle")
bgcolor("grey")

# Task 1 (Red circle)

color("red")
begin_fill()
circle(r)
end_fill()
# Task 2 (Russian national Flag)
color("white")

up()
goto(0, -100)
down()

# white part
fillcolor("white")
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


# blue part
fillcolor("blue")
right(90)
fd(50)
begin_fill()
fd(50)
left(90)
fd(200)
left(90)
fd(50)
right(90)
end_fill()


# red color

fillcolor("red")
right(90)
fd(50)
begin_fill()
fd(50)
right(90)
fd(200)
right(90)
fd(50)
# right(90)
end_fill()
exitonclick()