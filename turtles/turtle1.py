import turtle

window = turtle.Screen()
turtle.shape("turtle")
turtle.bgcolor("black")
turtle.pencolor("red")
turtle.speed(5)
turtle.pensize(2)

#risuem!

for i in 1,2,3,4:
    turtle.forward(100) # px
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)

#end

x = input()

turtle.exitonclick
