#=========================
# grid.py
#=========================

ROWS = 15
COLS = 16
CELL_SIZE = 40

GRID = [[0 for _ in range(COLS)] for _ in range(ROWS)]
GRID[0][0] = 2
GRID[ROWS-1][COLS-1] = 3

def find_value(value):
    for r in range(ROWS):
        for c in range(COLS):
            if GRID[r][c] == value:
                return (r, c)
    return None

def get_start():
    return find_value(2)

def get_goal():
    return find_value(3)

def reset_grid():
    for r in range(ROWS):
        for c in range(COLS):
            if GRID[r][c] in (2, 3):
                GRID[r][c] = 0
