from collections import defaultdict
import requests
import os
from dotenv import load_dotenv
load_dotenv()

pinput = requests.get('https://adventofcode.com/2023/day/15/input', cookies={"session": os.getenv("SESSION")}).text


def get_hash(s: str) -> int:
    curr_hash = 0
    for d in (ord(_c) for _c in s):
        curr_hash = (curr_hash + d) * 17 % 256
    return curr_hash


hashmap = defaultdict(list)

for step in pinput.split(','):
    step = step.strip('\n')
    add = False
    if '=' in step:
        name, val = step.split('=')
        val = int(val)
        add = True
    else:
        name = step.rstrip('-')
    box_num = get_hash(name)
    if add:
        for i in hashmap[box_num]:
            if i[0] == name:
                i[1] = val
                break
        else:
            hashmap[box_num].append([name, val])
    else:
        for i in hashmap[box_num]:
            if i[0] == name:
                hashmap[box_num].remove(i)
                break

tot_power = 0
for k, v in hashmap.items():
    if len(v) > 0:
        for i, (name, val) in enumerate(v):
            tot_power += (k+1) * (i+1) * val

print(tot_power)

