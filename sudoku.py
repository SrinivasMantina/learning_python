import numpy as np

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 2], [0, 0, 0, 0, 0, 0, 9, 4, 0], [0, 0, 3, 0, 0, 0, 0, 0, 5], 
    [0, 9, 2, 3, 0, 5, 0, 7, 4], [8, 4, 0, 0, 0, 0, 0, 0, 0], [0, 6, 7, 0, 9, 8, 0, 0, 0], 
    [0, 0, 0, 7, 0, 6, 0, 0, 0], [0, 0, 0, 9, 0, 0, 0, 2, 0], [4, 0, 8, 5, 0, 0, 3, 6, 0]
    ]

def is_possible(x, y, n):
    global grid
    for i in range(9):
        if grid[x][i] == n:
            return False
    for i in range(9):
        if grid[i][y] == n:
            return False
    p = (x // 3) * 3
    q = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[p+i][q+j] == n:
                return False
    return True

def solve_sudoku():
    global grid
    for x in range(9):
        for y in range(9):
            if grid[x][y] == 0:
                for n in range(1, 10):
                    if is_possible(x, y, n):
                        grid[x][y] = n
                        solve_sudoku()
                        grid[x][y] = 0
                return
    print(np.matrix(grid))

solve_sudoku()