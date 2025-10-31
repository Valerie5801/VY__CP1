#VY 2nd Maze Generator
import turtle #import turtle here
import random

#make a list of characters that look like walls as a placeholder
walls = ["|", "_"]

#make a list of characters with blank spaces as the places for where the things go
columns = [" ", " ", " ", " ", " ", " "] #this has six values for the six rows.

#Make a function for the maze generation 
def maze_gen(): #make a nested for loop for the square grid.
    rows = [] #make a list for the rows. This is for the grid.
    for column in columns:
        for i in range(1, 7):
            row = walls[random.randint(0, 1)]
            rows.append(column)
            return rows
        #print(columns)
        #rows = []
        

    
maze_gen()
#When having turtle draw the maze, make it do pendown, penup, at certain points to make the maze.

turtle.penup()
turtle.goto(x=-350, y=250)
turtle.pensize(5)
turtle.pendown()

turtle.done()