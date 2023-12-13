import requests
import os
from dotenv import load_dotenv
import functools

load_dotenv()
pinput = requests.get('https://adventofcode.com/2023/day/13/input', cookies={"session": os.getenv("SESSION")}).text
# pinput = """#.#........
# ##...#####.
# #.##..####.
# ##..##....#
# #..#.......
# #.#####..##
# .....#.##.#
# .###..#..#.
# ##..##....#
# ###..######
# ##.##.#..#.
# ..#####..##
# ###...#..#.
# .......##..
# #.#.##.##.#
# .#.##.#..#.
# .#.##.#..#.
#
# ..#.###
# #.#####
# #.#####
# ..#..##
# #......
# ##..###
# ..#....
# """


def get_patterns(inp: str):
    patterns = [p.splitlines() for p in inp.split('\n\n')]
    return patterns


def check_mirror(pattern: list[str], vert: bool = False):
    is_palindrome = lambda p: p == p[::-1]
    if vert:
        for i in range(1, len(pattern[0])):
            bwd, fwd = i, len(pattern[0]) - i
            check_len = min(bwd, fwd)
            if all(is_palindrome(pattern[j][i-check_len:i+check_len]) for j in range(len(pattern))):
                return i
        return 0
    else:
        for i in range(1, len(pattern)):
            bwd, fwd = i, len(pattern) - i
            check_len = min(bwd, fwd)
            if is_palindrome(pattern[i-check_len:i+check_len]):
                return i
        return 0


def main(inp: str):
    summary = 0
    for p in get_patterns(inp):
        v, h = check_mirror(p, True), check_mirror(p, False)
        summary += v
        summary += h * 100
    print(summary)


main(pinput)
