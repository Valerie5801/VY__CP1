#VY 2nd Maze Generator
import turtle #import turtle here
import random

#make a list of characters that look like walls as a placeholder
walls = ["|", "_", " "]

#make a list of characters with blank spaces as the places for where the things go
#columns = [" ", " ", " ", " ", " ", " "] #this has six values for the six rows.


rows = [
    [random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), random.randint(0, 2), choose_wall],
    [choose_wall, choose_wall, choose_wall, choose_wall, choose_wall, choose_wall],
    [choose_wall, choose_wall, choose_wall, choose_wall, choose_wall, choose_wall],
    [choose_wall, choose_wall, choose_wall, choose_wall, choose_wall, choose_wall],
    [choose_wall, choose_wall, choose_wall, choose_wall, choose_wall, choose_wall],
    [choose_wall, choose_wall, choose_wall, choose_wall, choose_wall, choose_wall]
]
#make a function for the maze generation
def maze_gen():
    for row in rows:
        for spot in rows:
            if spot:
                print("I STILL HATE EVERYTHING")
                continue
            else:
                print("I HATE EVERYTHING")

#def is_solvable(row_grid, col_grid):
 #   size = len(row_grid) - 1

#When having turtle draw the maze, make it do pendown, penup, at certain points to make the maze.