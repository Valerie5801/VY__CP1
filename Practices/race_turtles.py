#VY 2nd Turtle Race
import random #import libraries
import turtle

race_end = False #create a flag to signal when the program ends
#make the finish line on the right side at the start of the program.
finish = turtle.Turtle()
finish.hideturtle()
finish.color("black")
finish.pensize(10)
finish.penup()
finish.goto(x=400, y=-500)
finish.pendown()
finish.sety(500)
finish.isvisible()

#make a function that gives a different speed to each turtle
def speed():
    for competitor in competitors:
        competitor.forward(random.randint(1, 10))

#create all five turtles
red = turtle.Turtle()
blue = turtle.Turtle()
yellow = turtle.Turtle()
green = turtle.Turtle()
purple = turtle.Turtle()
competitors = [red, blue, yellow, green, purple]

#make a for loop to put general settings for each turtle
for competitor in competitors:
    competitor.hideturtle()
    competitor.shape("turtle")
    competitor.pensize(5)
    competitor.turtlesize(stretch_wid=3, stretch_len=3, outline=2)
    competitor.showturtle()

#setup turtle 1 (make it unique)
red.color("red")
red.penup()
red.goto(x=-490, y=430)
red.pendown()

#setup turtle 2
blue.color("blue")
blue.penup()
blue.goto(x=-490, y=230)
blue.pendown()

#setup turtle 3
yellow.color("yellow")
yellow.penup()
yellow.goto(x=-490, y=30)
yellow.pendown()

#setup turtle 4
green.color("green")
green.penup()
green.goto(x=-490, y=-200)
green.pendown()

#setup turtle 5
purple.color("purple")
purple.penup()
purple.goto(x=-490, y=-400)
purple.pendown()



#make an if statement to check what turtle won


turtle.done()