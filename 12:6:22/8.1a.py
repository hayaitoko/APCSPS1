import turtle
turtle.Turtle()

turtle.pensize(2)
turtle.color(0, 0, 0)
turtle.shape("classic")

for i in range(4):
    turtle.forward(100)
    for i in range(90):
        turtle.right(1)
        turtle.forward(1)
