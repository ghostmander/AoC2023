import re
from math import lcm

import requests
import os
from dotenv import load_dotenv

load_dotenv()
pinput = requests.get('https://adventofcode.com/2023/day/8/input', cookies={"session": os.getenv("SESSION")}).text


# pinput = """LR
#
# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""


def parse_input(inp: str) -> tuple[str, dict, list[str]]:
    movelist, _, *graph_definition = inp.splitlines()
    sources = set()
    graph = {}
    for definition in graph_definition:
        source, dest_left, dest_right = re.match(r'(\w+) = \((\w+), (\w+)\)', definition).groups()
        graph[source] = (dest_left, dest_right)
        if source[-1] == 'A':
            sources.add(source)
    return movelist, graph, [*sources]


def num_moves(movelist: str, graph: dict, sources: list[str]) -> int:
    def num_moves_single(path: str, move_map: dict, curr: str):
        moves = 0
        i = 0
        while curr[-1] != 'Z':
            curr = move_map[curr][(path[i] == 'R') & 1]
            moves += 1
            i += 1
            if i == len(path):
                i = 0
        return moves

    num_moves_per_source = []
    for source in sources:
        print(source, num_moves_single(movelist, graph, source))
        num_moves_per_source.append(num_moves_single(movelist, graph, source))
    return lcm(*num_moves_per_source)


print("Answer:", num_moves(*parse_input(pinput)))
