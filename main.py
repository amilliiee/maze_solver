from graphics import Window
from maze import Maze
import sys

def main():
    rows = 12
    cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / cols
    cell_size_y = (screen_y - 2 * margin) / rows

    sys.setrecursionlimit(1000)
    win = Window(screen_x, screen_y)

    maze = Maze(margin, margin, rows, cols, cell_size_x, cell_size_y, win, 10)
    print('Maze created')
    is_solv = maze.solve()
    if not is_solv:
        print('Maze can\'t be solved')
    else:
        print('Maze solved')

    win.wait_for_close()

main()