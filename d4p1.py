import requests
import os
from dotenv import load_dotenv
import re

load_dotenv()
inp = requests.get('https://adventofcode.com/2023/day/4/input', cookies={"session": os.getenv("SESSION")}).text
# inp = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""


def card_value(card: str) -> int:
    if not card:
        return 0
    winning_nos, nums_got = card.split(': ')[1].split(' | ')
    nums_got = [*filter(lambda x: x, (x for x in nums_got.strip().split(' ')))]
    wins = 0
    for i in winning_nos.strip().split(' '):
        wins += nums_got.count(i)
    if wins == 0:
        return 0
    return 2**(wins-1)


print(sum(card_value(c) for c in inp.strip('\n').split('\n')))
