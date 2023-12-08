import re

import requests
import os
from dotenv import load_dotenv

load_dotenv()
pinput = requests.get('https://adventofcode.com/2023/day/8/input', cookies={"session": os.getenv("SESSION")}).text
# pinput = """RL
#
# AAA = (BBB, CCC)
# BBB = (DDD, EEE)
# CCC = (ZZZ, GGG)
# DDD = (DDD, DDD)
# EEE = (EEE, EEE)
# GGG = (GGG, GGG)
# ZZZ = (ZZZ, ZZZ)"""


def parse_input(inp: str) -> tuple[str, dict]:
    movelist, _, *graph_definition = inp.splitlines()
    graph = {}
    for definition in graph_definition:
        source, dest_left, dest_right = re.match(r'(\w+) = \((\w+), (\w+)\)', definition).groups()
        graph[source] = (dest_left, dest_right)
    return movelist, graph


def num_moves(movelist: str, graph: dict, source: str = 'AAA', dest: str = 'ZZZ') -> int:
    moves = 0
    curr = source
    i = 0
    while curr != dest:
        if movelist[i] == 'L':
            curr = graph[curr][0]
        else:
            curr = graph[curr][1]
        moves += 1
        i += 1
        if i == len(movelist):
            i = 0
    return moves


print(num_moves(*parse_input(pinput)))
