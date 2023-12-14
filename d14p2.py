import requests
import os
from dotenv import load_dotenv
load_dotenv()
pinput = requests.get('https://adventofcode.com/2023/day/14/input', cookies={"session": os.getenv("SESSION")}).text
curr = pinput.strip('\n')

transpose = lambda x: [''.join(_i) for _i in zip(*x)]
boards = {curr: iter}
cs, cl = None, None
for i in range(1000000000):
    curr = ('#'.join(''.join(sorted(i, reverse=True)) for i in r.split('#')) for r in transpose(curr.splitlines()))
    curr = ('#'.join(''.join(sorted(i, reverse=True)) for i in r.split('#')) for r in transpose(curr))
    curr = ('#'.join(''.join(sorted(i)) for i in r.split('#')) for r in transpose(curr))
    curr = '\n'.join('#'.join(''.join(sorted(i)) for i in r.split('#')) for r in transpose(curr))
    if curr in boards:
        cs, cl = boards[curr], i - boards[curr]
        break
    else:
        boards[curr] = i

print(sum(r.count('O') * i for i, r in enumerate([*boards.keys()][cs + (1000000000 - cs) % cl].splitlines()[::-1], 1)))
