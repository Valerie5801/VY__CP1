#VY 2nd Turtle Drawing starter
#import turtle module
import turtle

#define function draw_branch(length):
def draw_branch(length):
    if length > 5:
        for i in range(3):
            turtle.forward(length)
            draw_branch(length/3)
            turtle.backward(length)
            turtle.right(60)

#set up turtle:
turtle.speed(0)
turtle.color("light blue")
turtle.penup()
turtle.goto(x=0, y=0)
turtle.pendown()

#main snowflake drawing:
for i in range(6):
    draw_branch(100)
    turtle.right(60)

turtle.done()