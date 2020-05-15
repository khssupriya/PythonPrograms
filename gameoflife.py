import random
import time
import os
import math
import numpy as np
from copy import deepcopy

ROWS = 50
COLS = 50
grid = [[0 for j in range(COLS)] for i in range(ROWS)]
def set_up_grid():
    for i in range(ROWS):
        for j in range(COLS):
            grid[i][j] = random.randint(0,1)

def print_grid():
    time.sleep(0.02)
    os.system("clear")
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j]:
                print("#",end=" ")
            else:
                print(" ",end=" ")
        print()
            

def update_grid():
    curr_grid = deepcopy(grid)
    for i in range(ROWS):
        for j in range(COLS):
            if i == 0 or i == ROWS -1 or j == 0 or j == COLS - 1:
                continue
            live_neighbours = count_neighbours(i, j, curr_grid)
            state = grid[i][j]
            if state == 0 and live_neighbours == 3:
                grid[i][j] = 1
            elif state == 1 and (not live_neighbours in [2,3]) :
                grid[i][j] = 0
    print_grid()

def count_neighbours(x, y, grid):
    neighbours = -grid[x][y]
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            neighbours += grid[x+i][y+j]
    return neighbours

if __name__ == "__main__":
    set_up_grid()
    print_grid()
    update_grid()
    i = 0
    while True:
        update_grid()
        i += 1
        if i > 50:
            break


