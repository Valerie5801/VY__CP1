#VY 2nd Maze Generator
import turtle #import turtle here
import random

#make two lists inside of a list; one for the rows and one for the columns. use random.randint to for 0 or 1 (no wall or wall.)
rows = [
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]
]

columns = [
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]
]

#create a function for the maze generation.
def maze_gen():
    turtle.speed(0.5)
    turtle.penup()
    turtle.goto(x=-300, y=-250)
    count_row = 0 #counter for how many rows the turtle has completed
    count_col = 0 #counter for how many columns the turtle has completed
    for i in range(2):
        for row in rows:
            for spot in row:
                if spot == 0: #don't draw if that spot is a 0
                    turtle.penup()
                    turtle.forward(50)
                elif spot == 1: #don't draw if that spot is a 1
                    turtle.pendown()
                    turtle.forward(50)
                    turtle.penup()
            count_row += 1
            turtle.goto(x=-300, y=-250+(count_row*25))
    turtle.penup()
    turtle.goto(x=-300, y=0)
    turtle.right(90)
    for i in range(2):
        for column in columns:
            for spot in column:
                if spot == 0:
                    turtle.penup()
                    turtle.forward(50)
                elif spot == 1:
                    turtle.pendown()
                    turtle.forward(50)
                    turtle.penup()
            count_col += 1
            turtle.goto(x=-300+(count_col*25), y=0)


turtle.screensize(canvwidth=50, canvheight=50)
turtle.penup()
turtle.goto(x=-300, y=-300)
turtle.pendown()
for i in range(4):
    turtle.forward(25)
    if turtle.ycor() == -300 or turtle.ycor() == 0:
        turtle.penup()
        turtle.forward(25)
        turtle.pendown()
        turtle.forward(250)
    else:
        turtle.forward(275)
    turtle.right(-90)
maze_gen()
turtle.done()
#def is_solvable(row_grid, col_grid):
 #   size = len(row_grid) - 1
    #visited = set()
    #stack = [(0, 0)]
    
    #while stack:
        #x, y = stack.pop()

        #if x == size - 1 and y == sizee - 2:
            #return True
        
        #if (x, y) in visited:
            #continue

        #visited.add((x, y))

        #if x < size - 1 and columns[y][x+1] == 0:
            #stack.append((x+1, y))

        #if y < size - 1 and rows[y][x+1] == 0:
            #stack.append((x, y+1))
        
        #if x > 0 and columns[y][x] == 0:
            #stack.append((x-1, y))
        
        #if y > 0 and rows[y][x] == 0:
            #stack.append((x, y-1))

    #return False

#When having turtle draw the maze, make it do pendown, penup, at certain points to make the maze.