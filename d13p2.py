import requests
import os
from dotenv import load_dotenv
import functools

load_dotenv()
pinput = requests.get('https://adventofcode.com/2023/day/13/input', cookies={"session": os.getenv("SESSION")}).text


# pinput = """#.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.
#
# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#
# """


def get_smudges(pattern):
    patterns = []
    # ALL patterns with exactly one opposite value (# -> . and . -> #)
    for i in range(len(pattern)):
        for j in range(len(pattern[0])):
            c = '.' if pattern[i][j] == '#' else '#'
            patterns.append(pattern[:i] + [pattern[i][:j] + c + pattern[i][j + 1:]] + pattern[i + 1:])
    return patterns


def print_pattern(pattern):
    print('\n'.join(pattern))


def check_mirror(pattern: list[str], vert: bool = False):
    if vert:
        pattern = [*zip(*pattern)]
    for i in range(1, len(pattern)):
        if sum(c1 != c2 for r1, r2 in zip(pattern[i - 1::-1], pattern[i:]) for c1, c2 in zip(r1, r2)) == 1:
            return i
    return 0


def main(inp: str):
    summary = 0
    for p in [p.splitlines() for p in inp.split('\n\n')]:
        v, h = check_mirror(p, True), check_mirror(p, False)
        summary += v
        summary += h * 100
    print(summary)
    # summary = 0
    # for base_p in [p.splitlines() for p in inp.split('\n\n')]:
    #     v_base, h_base = check_mirror(base_p, True), check_mirror(base_p, False)
    #     for p in get_smudges(base_p):
    #         v, h = check_mirror(p, True), check_mirror(p, False)
    #         if v_base == v:
    #             v = 0
    #         if h_base == h:
    #             h = 0
    #         if v or h:
    #             print_pattern(p)
    #             print(v, h)
    #             print()
    #             summary += h * 100
    #             summary += v
    #             break
    # print(summary)


main(pinput)
