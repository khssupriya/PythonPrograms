LF = "\n"
BLACK, WHITE = "#", "_"
TO_NUMBER = BLACK + WHITE + WHITE

def add_sentinels(grid: [str]) -> [str]:
    size = len(grid[0])
    sentinel_grid = [BLACK + row + BLACK for row in grid]
    sentinel_grid.append((size+2) * BLACK)
    sentinel_grid.insert(0,(size+2) * BLACK)
    return sentinel_grid

# def clue_locations(grid: [str], orientation = "ACROSS")->[str]:    #complex version
#     width = len(grid[0])
#     one_line_grid = ''.join(grid)
#     start = 0
#     clue_starts = []
#     at = one_line_grid.find(TO_NUMBER, start)
#     while at != -1:
#         clue_starts.append(divmod(at + 1, width))
#         start = at + 2
#         at = one_line_grid.find(TO_NUMBER, start)
#     return clue_starts

def clue_locations(grid: [str])->[(int,int)]:         #simple version
    clue_starts=set()
    for row, line in enumerate(grid):
        for col, cell in enumerate(line):
            if line[col-1:col+2] == TO_NUMBER:
                clue_starts.add((row, col))
            if grid[row-1][col] + grid[row][col] + grid[row+1][col] == TO_NUMBER:
                clue_starts.add((row,col))
    return list(sorted(clue_starts))

input_grid=[line.strip() for line in open("xyz.txt")]
new_grid = add_sentinels(input_grid)
ac_clues = clue_locations(new_grid)
# xpose = [''.join(x) for x in zip(*new_grid)]
# dn_clues = clue_locations(xpose, "DOWN")
# clues = list(sorted(ac_clues)|set(dn_clues))
print(ac_clues)