import matplotlib.path
import requests
import os
from dotenv import load_dotenv

load_dotenv()
inp = requests.get('https://adventofcode.com/2023/day/10/input', cookies={"session": os.getenv("SESSION")}).text
# inp = """..F7.
# .FJ|.
# SJ.L7
# |F--J
# LJ...
# """

MOVES = {
    '|': ((1, 0), (-1, 0)),
    '-': ((0, -1), (0, 1)),
    'L': ((-1, 0), (0, 1)),
    'J': ((-1, 0), (0, -1)),
    '7': ((0, -1), (1, 0)),
    'F': ((1, 0), (0, 1)),
}


def process_input(inp: str) -> tuple:
    grid = []
    for line in inp.splitlines():
        if 'S' in line:
            start = (len(grid), line.index('S'))
        grid.append(list(line))
    return grid, start


def main(grid: list, start: tuple):
    sx, sy = start
    start_move = set(MOVES.keys())
    if sy < len(grid[sx]) - 1 and grid[sx][sy+1] in '-7J':
        start_move = start_move.intersection(set(list('-LF')))
    if sy > 0 and grid[sx][sy-1] in '-LF':
        start_move = start_move.intersection(set(list('-7J')))
    if sx < len(grid) - 1 and grid[sx+1][sy] in '|LJ':
        start_move = start_move.intersection(set(list('|F7')))
    if sx > 0 and grid[sx-1][sy] in '|F7':
        start_move = start_move.intersection(set(list('|LJ')))
    start_move = start_move.pop()
    grid[sx][sy] = start_move

    def get_connection(x, y):
        return [(x+dx, y+dy) for dx, dy in MOVES[grid[x][y]]]

    seen = {start}
    path = [[*start]]
    curr = start
    while True:
        conns = get_connection(*curr)
        for conn in conns:
            if conn not in seen:
                seen.add(conn)
                path.append([*conn])
                curr = conn
                break
        else:
            print(curr)
            break
        if curr == start:
            break
    polygon = matplotlib.path.Path(path)
    num = sum(1 for y in range(1, len(grid) - 1) for x in range(1, len(grid[0]) - 1)
              if (c := (y, x)) not in seen and polygon.contains_point(c))
    print('P2 =', num)

    print(len(seen))
    # print_grid(grid, seen)




def print_grid(grid: list, seen = set()):
    g1 = []
    for x, line in enumerate(grid):
        capturing = False
        g1.append([])
        for y, char in enumerate(line):
            if not capturing:
                g1[-1].append('.')
            else:
                g1[-1].append(char)
            if (x, y) in seen:
                g1[-1][-1] = '█'
                capturing = not capturing

    g = '\n'.join(''.join(line) for line in g1)
    g = (g.replace('F', '╭').replace('7', '╮').replace('-', '─').replace('|', '│')
          .replace('L', '╰').replace('J', '╯').replace('.', ' '))
    print(g)



grid, start = process_input(inp)
main(grid, start)
