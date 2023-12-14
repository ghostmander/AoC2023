import requests
import os
from dotenv import load_dotenv
load_dotenv()
inp = requests.get('https://adventofcode.com/2023/day/14/input', cookies={"session": os.getenv("SESSION")}).text
tilt = lambda x: [''.join(_i) for _i in zip(*x)]
n = tilt('#'.join(''.join(sorted(i, reverse=True)) for i in r.split('#')) for r in tilt(inp.splitlines()))
print(sum(r.count('O') * i for i, r in enumerate(n[::-1], 1)))
