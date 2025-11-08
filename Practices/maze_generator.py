#VY 2nd Maze Generator
import turtle #import turtle here
import random

#make a function to put random values inside of the rows and columns lists
def maze_gen():
    #make two lists inside of a list; one for the rows and one for the columns. make each list inside of the list empty so we can randomize them (for the walls) any time we want. These are like blank slates. This square will be a 12x12 because of the size of the square, and by doing a 6x6 and the nested for loop run twice will make the maze be repetitive.
    rows = [ #12 lists inside of each list because its a 12x12
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]
    columns = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]
    size = 12 #this is a 12x12 grid
    for row in rows:
        for i in range(12): #since this is a 12x12 square, this must run 12 times to fill all spots
            row.append(random.randint(0, 1))
    for column in columns:
        for i in range(12): #same thing here
            column.append(random.randint(0, 1))
    x, y = 0, 0
    path_coords = set()
    while x < size - 1 or y < size - 1:
        path_coords.add((x, y))
        if x < size - 1 and (y == size - 1 or random.choice([True, False])):
            columns[x][y] = 0
            x += 1
        elif y < size - 1:
            rows[x][y] = 0
            y += 1
    path_coords.add((11, 11))
    rows[0][0] = 0 #entrance
    columns[0][0] = 0
    rows[size-1][size-1] = 0
    columns[size-1][size-1] = 0 #exit

    for i in range(size):
        for j in range(size):
            if (i, j) not in path_coords:
                rows[i][j] = random.randint(0, 1)
                columns[i][j] = random.randint(0, 1)

    return rows, columns #this returns with index values so we can access each one. row_grid's index is 0 while col_grid is a 1.

#create a function to check if the maze is solvable.
def is_solvable(grid):
    row_grid, col_grid = grid #to improve readability, set rows to grid[0] and columns to grid[1]
    size = len(row_grid) #a size of 12
    visited = set() #empty list for coordinates that have already been visited
    stack = [(0, 0)]
    
    while stack:
        x, y = stack.pop() #replace the 0, 0 in stack with x, y

        if x == size - 1 and y == size - 1:
            return True
        
        if (x, y) in visited: #check if we've been here before
            continue

        visited.add((x, y)) #add this spot to the "we've been here before" list

        if x < size - 1 and col_grid[x][y] == 0: #check the spot to the right for a wall. We are going into the column list for this.
            stack.append((x+1, y))

        if y < size - 1 and row_grid[x][y] == 0: #check the spot upwards for a wall
            stack.append((x, y+1))
        
        if x > 0 and col_grid[x-1][y] == 0: #check the spot leftwards for a wall
            stack.append((x-1, y))
        
        if y > 0 and row_grid[x][y-1] == 0: #check the spot downwards for a wall
            stack.append((x, y-1))

    return False #return false if we have checked every index and there is no exit

#create a function for the maze generation.
def draw_maze(grid):
    turtle.speed(0)
    turtle.penup()
    turtle.goto(x=0, y=25) #go near the bottom left corner (not the bottom since we don't want it to draw over the entrance and face right to start drawing rows.
    count_row = 0 #counter for how many rows the turtle has completed
    count_col = 0 #counter for how many columns the turtle has completed
    for row in grid[0]: #make a nested loop for drawing rows
        if count_row == 11:#check if we are on the final row, which is actually the top side. If we are, make turtle guarantee that there is a gap in the wall (make sure turtle doesn't draw over the gap)
            break
        for spot in row:
            if spot == 0: #don't draw if that spot is a 0
                turtle.penup()
                turtle.forward(25)
            elif spot == 1: #draw if that spot is a 1
                turtle.pendown()
                turtle.forward(25)
                turtle.penup()
        count_row += 1 #add one for each row the turtle completes
        turtle.goto(x=0, y=25+(count_row*25))
    turtle.penup()
    turtle.goto(x=25, y=0) #go to the bottom left corner and face up to start drawing columns
    turtle.right(-90)
    for column in grid[1]: #make a nested for loop for drawing the columns.
        for spot in column:
            if spot == 0: #don't draw if spot is 0
                turtle.penup()
                turtle.forward(25)
            elif spot == 1: #draw if spot is a 1
                turtle.pendown()
                turtle.forward(25)
                turtle.penup()
        count_col += 1 #add one for each column the turtle completes
        turtle.goto(x=25+(count_col*25), y=0)
    turtle.hideturtle() #hide the turtle after it finished drawing everything.


def final_maze(): #this function will be ran every time the user wants a new maze.
    while True:
        maze = maze_gen() #run the function and set it's value to a variable
        if is_solvable(maze): #is_solvable returns a boolean
            draw_maze(maze)
            break
        elif not is_solvable(maze):
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
final_maze()
turtle.done()
