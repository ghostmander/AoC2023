import requests
import os
from dotenv import load_dotenv

load_dotenv()
inp = requests.get('https://adventofcode.com/2023/day/1/input', cookies={"session": os.getenv("SESSION")}).text


def process_line(line):
    if not line:
        return 0
    line = (line.replace('one', 'o1e').replace('two', 't2o').replace('three', 't3e').replace('four', '4')
            .replace('five', 'f5e').replace('six', '6').replace('seven', '7n').replace('eight', 'e8t').replace('nine',
                                                                                                               'n9e'))
    digs = [c for c in line.strip() if c.isdigit()]
    num = digs[0] + digs[-1]
    return int(num)


print(sum(process_line(line) for line in inp.split('\n')))
