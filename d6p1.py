import requests
import os
from dotenv import load_dotenv

load_dotenv()
inp = requests.get('https://adventofcode.com/2023/day/6/input', cookies={"session": os.getenv("SESSION")}).text

inp = """Time:      7  15   30
Distance:  9  40  200"""


def process_input(s):
    s = s.strip('\n').split('\n')
    time = list(map(int, s[0].split(':')[1].strip().split()))
    distance = list(map(int, s[1].split(':')[1].strip().split()))
    return [*zip(time, distance)]


def num_above(total_time: int, curr_max: int) -> int:
    num = 0
    for i in range(0, total_time):
        if i * (total_time - i) > curr_max:
            break
        num += 1
    return total_time+1-num*2


prod = 1
for t, d in process_input(inp):
    prod *= num_above(t, d)
print(prod)
