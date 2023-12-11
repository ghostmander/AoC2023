import requests
import os
from dotenv import load_dotenv
import itertools

load_dotenv()
inp = requests.get('https://adventofcode.com/2023/day/11/input', cookies={"session": os.getenv("SESSION")}).text
inp = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""


def process_input(inp: str) -> list:
    inp_lines = inp.splitlines()
    galaxies = []
    x, y = 0, 0
    empty_rows = [i for i, line in enumerate(inp_lines) if '#' not in line]
    empty_cols = [i for i in range(len(inp_lines[0])) if all(inp_lines[x][i] == '.' for x in range(len(inp_lines)))]
    for i, line in enumerate(inp_lines):
        x += (i in empty_rows)
        y = 0
        for j, c in enumerate(line):
            y += (j in empty_cols)
            if c == '#':
                galaxies.append((x, y))
            y += 1
        x += 1
    return galaxies


get_distance = lambda g1, g2: abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])


def main(galaxies: list):
    # for g1, g2 in itertools.combinations(galaxies, 2):
    #     print(galaxies.index(g1) + 1, galaxies.index(g2) + 1, " -> ", get_distance(g1, g2))
    total_distances = [get_distance(g1, g2) for g1, g2 in itertools.combinations(galaxies, 2)]
    print(sum(total_distances))
    # print(len(total_distances))


g = process_input(inp)
main(g)
