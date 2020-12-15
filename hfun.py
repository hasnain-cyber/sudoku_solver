from constants import *


def verify(x, y, n, grid):
    for l1 in range(9):
        if grid[x][l1] == n:
            return False
    for l2 in range(9):
        if grid[l2][y] == n:
            return False
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for l1 in range(3):
        for l2 in range(3):
            if grid[l1 + x0][l2 + y0] == n:
                return False
    return True


def get_tile(mouse):
    x = mouse[0]
    y = mouse[1]
    return (x // rect_width) * rect_width, (y // rect_width) * rect_width
