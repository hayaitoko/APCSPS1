import turtle
import time

turtle.Turtle()
turtle.width(7)

turtle.begin_fill()
turtle.circle(50)
turtle.end_fill

turtle.penup()
turtle.setpos(75, 50)
turtle.pendown()

turtle.begin_fill()
for x in range(0, 4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
