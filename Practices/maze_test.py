# Headless tester for maze generation
# Reimplements the current maze_gen + is_solvable logic from maze_generator.py
import random

def maze_gen(size=12):
    rows = [[] for _ in range(size)]
    columns = [[] for _ in range(size)]
    for row in rows:
        for i in range(size):
            row.append(random.randint(0,1))
    for column in columns:
        for i in range(size):
            column.append(random.randint(0,1))
    # Build an explicit monotonic path from (0,0) to (size-1,size-1)
    moves = ['R'] * (size - 1) + ['U'] * (size - 1)
    random.shuffle(moves)

    x, y = 0, 0
    for m in moves:
        if m == 'R':
            # open vertical wall between (x,y) and (x+1,y)
            columns[x][y] = 0
            x += 1
        else:  # 'U'
            # open horizontal wall between (x,y) and (x,y+1)
            rows[x][y] = 0
            y += 1

    # Ensure entrance and exit are clear
    rows[0][0] = 0
    columns[0][0] = 0
    rows[size-1][size-1] = 0
    columns[size-1][size-1] = 0

    return rows, columns

def is_solvable(grid):
    row_grid, col_grid = grid
    size = len(row_grid)
    visited = set()
    stack = [(0,0)]
    while stack:
        x,y = stack.pop()
        if x == size-1 and y == size-1:
            return True
        if (x,y) in visited:
            continue
        visited.add((x,y))
        if x < size-1 and col_grid[x][y] == 0:
            stack.append((x+1,y))
        if y < size-1 and row_grid[x][y] == 0:
            stack.append((x,y+1))
        if x > 0 and col_grid[x-1][y] == 0:
            stack.append((x-1,y))
        if y > 0 and row_grid[x][y-1] == 0:
            stack.append((x,y-1))
    return False

if __name__ == '__main__':
    trials = 2000
    fail_examples = []
    for t in range(trials):
        g = maze_gen()
        if not is_solvable(g):
            fail_examples.append(g)
            if len(fail_examples) >= 3:
                break
    print(f"Trials: {trials}, failures: {len(fail_examples)}")
    if fail_examples:
        print("Showing first failing example (rows then columns):")
        r,c = fail_examples[0]
        for row in r:
            print(''.join(str(x) for x in row))
        print("---")
        for col in c:
            print(''.join(str(x) for x in col))
