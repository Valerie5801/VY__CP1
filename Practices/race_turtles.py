#VY 2nd Turtle Race
import random #import libraries
import turtle

race_end = False #create a flag to signal if a turtle won or not
#make a function for the finish line
finish = turtle.Turtle()
def create_race():
    finish.hideturtle()
    finish.color("red")
    finish.pensize(5)
    finish.penup()
    finish.goto(x=400, y=-500)
    finish.pendown()
    finish.sety(500)
    finish.isvisible()
    finish.screen.title("Turtle race!")

#create all five turtles
red = turtle.Turtle()
blue = turtle.Turtle()
yellow = turtle.Turtle()
green = turtle.Turtle()
purple = turtle.Turtle()
competitors = [red, blue, yellow, green, purple]

#make a function that creates each turtle
def creation(turt_name):
    turt_name.shape("turtle")
    turt_name.pensize(5)
    turt_name.turtlesize(stretch_wid=3, stretch_len=3, outline=2)

#make a function that makes each turtle go a random amount of steps in one round
def movement():
    for competitor in competitors:
        competitor.forward(random.randint(1, 10))


#setup turtle 1 (make it unique)
creation(red)
red.color("red")
red.penup()
red.goto(x=-490, y=430)
red.pendown()

#setup turtle 2
creation(blue)
blue.color("blue")
blue.penup()
blue.goto(x=-490, y=230)
blue.pendown()

#setup turtle 3
creation(yellow)
yellow.color("yellow")
yellow.penup()
yellow.goto(x=-490, y=30)
yellow.pendown()

#setup turtle 4
creation(green)
green.color("green")
green.penup()
green.goto(x=-490, y=-200)
green.pendown()

#setup turtle 5
creation(purple)
purple.color("purple")
purple.penup()
purple.goto(x=-490, y=-400)
purple.pendown()

#create the finish line
create_race()

#make a while loop for the race itself
while not race_end:
    movement()
    #make an if statement to check what turtle won
    if red.xcor() >= finish.xcor():
        red.screen.title("Red wins.")
        break
    if blue.xcor() >= finish.xcor():
        blue.screen.title("Blue wins.")
        break
    if yellow.xcor() >= finish.xcor():
        yellow.screen.title("Yellow wins.")
        break
    if green.xcor() >= finish.xcor():
        green.screen.title("Green wins.")
        break
    if purple.xcor() >= finish.xcor():
        purple.screen.title("Purple wins.")
        break
    else:
        continue


turtle.done()