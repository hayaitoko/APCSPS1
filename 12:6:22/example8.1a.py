import turtle
import time

turtle.Turtle()
time.sleep(2)
turtle.color("Blue")
turtle.pensize(2)
turtle.shape("turtle")

turtle.left(90)
time.sleep(2)
turtle.forward(50)
time.sleep(2)
time.sleep(2)
turtle.right(90)
time.sleep(2)
turtle.forward(50)
for x in range(4):
    turtle.forward(50)
    turtle.left(90)
    time.sleep(2)