#VY 2nd Maze Generator
import turtle #import turtle here
import random

#make two lists inside of a list; one for the rows and one for the columns. use random.randint to for 0 or 1 (no wall or wall.)
rows = [
    [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2)],
    [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2)],
    [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2)],
    [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2)],
    [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2)],
    [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2)]
]

columns = [
    [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2)],
    [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2)],
    [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2)],
    [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2)],
    [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2)],
    [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2)]
]

#create a function for the maze generation.
def maze_gen():
    count_col = 0
    count_row = 0
    turtle.penup()
    turtle.goto(x=-250, y=-250)
    for row in rows:
        for spot in row:
            if spot > 0:
                turtle.forward(25)
                turtle.penup()
            else:
                turtle.penup()
                turtle.forward(25)
        count_row += 1
        turtle.goto(x=-250, y=-250+(count_row*25))
        turtle.pendown()
    turtle.goto(x=-250, y=0)
    turtle.right(90)
    for column in columns:
        for spot in column:
            if spot > 0:
                turtle.forward(25)
                turtle.penup()
            else:
                turtle.penup()
                turtle.forward(25)
        count_col += 1
        turtle.goto(x=-250+(count_col*25), y=-150)
        turtle.pendown()


turtle.screensize(canvwidth=500, canvheight=500)
maze_gen()
turtle.done()
#def is_solvable(row_grid, col_grid):
 #   size = len(row_grid) - 1

#When having turtle draw the maze, make it do pendown, penup, at certain points to make the maze.