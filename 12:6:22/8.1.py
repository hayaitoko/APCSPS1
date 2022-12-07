import turtle
turtle.Turtle()

turtle.pensize(2)
turtle.color(255, 255, 255)
turtle.shape("classic")

def square(length):
   turtle.forward(length)
   turtle.right(90)

x = int(input("enter side length: "))

for i in range(4):
   square(x)