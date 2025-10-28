#VY 2nd Turtle Race
import random #import libraries
import turtle

#create turtle 1
    #set position for this turtle and all other turtles
red = turtle.Turtle()
red.color("red")
red.shape("turtle")
red.teleport(x=-100, y=250, fill_gap=False)

#create turtle 2
blue = turtle.Turtle()
blue.color("blue")
blue.shape("turtle")

#create turtle 3
yellow = turtle.Turtle()
yellow.color("yellow")
yellow.shape("turtle")

#create turtle 4
green = turtle.Turtle()
green.color("green")
green.shape("turtle")

#create turtle 5
purple = turtle.Turtle()
purple.color("purple")
purple.shape("turtle")

#Make each turtle have different speeds
#Make a finish line on the right side of the screen
turtle.done()