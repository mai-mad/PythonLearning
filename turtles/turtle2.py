import turtle

r=200

window = turtle.Screen()
turtle.shape("turtle")
turtle.bgcolor("black")
turtle.pencolor("red")
turtle.speed(12)
turtle.pensize(2)

#risuem!
for i in range(36):
    turtle.circle(r)
    turtle.left(10)

turtle.pencolor("yellow")
turtle.left(3)
for i in range(36):
    turtle.circle(r)
    turtle.left(10)

turtle.pencolor("green")
turtle.left(3)
for i in range(36):
    turtle.circle(r)
    turtle.left(10)


turtle.pencolor("blue")
turtle.left(3)
for i in range(36):
    turtle.circle(r)
    turtle.left(10)

#end

x = input()

turtle.exitonclick
