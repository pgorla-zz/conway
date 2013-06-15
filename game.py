#!/usr/bin/env python

ROWS = 3
ROW_WIDTH = 3

CELLS = [[1,1,0],
         [1,0,0],
         [0,0,0]]

NEW_CELLS = CELLS

live_to_next = False

def run(gen=5):
    for i in range(0, gen):
        _run(gen)

def _run(gen):
    global CELLS
    for row in CELLS:
        print row
    for i in range(0, ROWS):
        for j in range(0, ROW_WIDTH):
            NEW_CELLS[i][j] = get_cell(i,j)
    CELLS = NEW_CELLS
    print

def get_cell(i,j):
    return lt_two_neighbors(i,j)

def lt_two_neighbors(i,j):
    """Any live cell with less than 2 neighbors dies."""
    neighbors = 0
    neighbor_left = [i+1, i-1]
    neighbor_right = [j+1, j-1]
    for n in neighbor_left:
        try:
            neighbors += CELLS[n][j]
        except IndexError: pass
    for n in neighbor_right:
        try:
            neighbors += CELLS[i][n]
        except IndexError: pass
    if neighbors >= 2:
        return 1
    return 0

if __name__ == "__main__":
    run()
