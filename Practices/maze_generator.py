#VY 2nd Maze Generator
import turtle #import turtle here
import random

#make two lists inside of a list; one for the rows and one for the columns. use random.randint to for 0 or 1 (no wall or wall.)
rows = [
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]
]

columns = [
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)],
    [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]
]

#create a function to check if the maze is solvable.
def is_solvable(row_grid, col_grid):
    size = len(row_grid) - 1
    visited = set() #empty list for coordinates that have already been visited
    stack = [(0, 0)]
    
    while stack:
        x, y = stack.pop() #replace the 0, 0 in stack with x, y

        if x == size - 1 and y == size - 2:
            return True
        
        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x < size - 1 and col_grid[y][x+1] == 0: #check the spot to the right for a wall
            stack.append((x+1, y))

        if y < size - 1 and row_grid[y][x+1] == 0: #check the spot upwards for a wall
            stack.append((x, y+1))
        
        if x > 0 and col_grid[y][x] == 0: #check the spot leftwards for a wall
            stack.append((x-1, y))
        
        if y > 0 and row_grid[y][x] == 0: #check the spot downwards for a wall
            stack.append((x, y-1))

    return False #return false if we have checked every index and there is no exit

#create a function for the maze generation.
def draw_maze():
    turtle.speed(0.5)
    turtle.penup()
    turtle.goto(x=0, y=25) #go near the bottom left corner (not the bottom since we don't want it to draw over the entrance and face right to start drawing rows.
    count_row = 0 #counter for how many rows the turtle has completed
    count_col = 0 #counter for how many columns the turtle has completed
    for i in range(2): #make a nested loop for drawing rows
        for row in rows:
            for spot in row:
                if spot == 0: #don't draw if that spot is a 0
                    turtle.penup()
                    turtle.forward(50)
                elif spot == 1: #draw if that spot is a 1
                    turtle.pendown()
                    turtle.forward(50)
                    turtle.penup()
            count_row += 1 #add one for each row the turtle completes
            turtle.goto(x=0, y=0+(count_row*25))
    turtle.penup()
    turtle.goto(x=0, y=300) #go to the top left corner and face down to start drawing columns
    turtle.right(90)
    for i in range(2): #make a nested for loop for drawing the columns.
        for column in columns:
            for spot in column:
                if spot == 0: #don't draw if spot is 0
                    turtle.penup()
                    turtle.forward(50)
                elif spot == 1: #draw if spot is a 1
                    turtle.pendown()
                    turtle.forward(50)
                    turtle.penup()
            count_col += 1 #add one for each column the turtle completes
            turtle.goto(x=0+(count_col*25), y=300)


def final_maze():
    while True:
        if is_solvable(rows, columns):
            draw_maze()
            break
        else:
            continue

turtle.screensize(canvwidth=50, canvheight=50) #create screensize
turtle.penup()
turtle.goto(x=0, y=0) #starting point of drawing the outside of the maze, and drawing the inside of the maze, and the starting point of the maze.
turtle.pendown()
for i in range(4): #make a loop that makes a square
    turtle.forward(25) #go forward a little bit in case there is a gap
    if turtle.ycor() == 0 or turtle.ycor() == 300: #if the turtle is on the top or bottom sides, make a gap. On the bottom side, it will make a gap on the left side, and on the top, it will make a gap on the right side.
        turtle.penup()
        turtle.forward(25)
        turtle.pendown()
        turtle.forward(250)
    else: #if not, just draw a straight line.
        turtle.forward(275)
    turtle.right(-90)
draw_maze()
turtle.done()
