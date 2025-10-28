#VY 2nd Libraries Notes
import random
import turtle

number = random.randint(100, 500)

turtle.color("#000000")
turtle.pensize(10)
turtle.shape("turtle")
turtle.turtlesize(stretch_wid=50, stretch_len=50, outline=2)

turtle.fillcolor("blue")
turtle.begin_fill()
for x in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(-50, 100)
turtle.pendown()
turtle.fillcolor("blue")
turtle.begin_fill()
for x in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()

turtle.done()