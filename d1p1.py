import requests
import os
from dotenv import load_dotenv

load_dotenv()
inp = requests.get('https://adventofcode.com/2023/day/1/input', cookies={"session": os.getenv("SESSION")}).text
inp = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""


def process_line(line):
    if not line:
        return 0
    digs = [c for c in line.strip() if c.isdigit()]
    num = digs[0] + digs[-1]
    return int(num)


print(sum(process_line(line) for line in inp.split('\n')))