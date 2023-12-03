import requests
import os
from dotenv import load_dotenv
import re

load_dotenv()
inp = requests.get('https://adventofcode.com/2023/day/3/input', cookies={"session": os.getenv("SESSION")}).text


def sum_part_nos(s: str) -> int:
    part_nos = []
    s = s.strip('\n').split('\n')
    for i, line in enumerate(s):
        j = 0
        while j < len(line):
            c = line[j]
            if c.isdigit():
                j1 = j
                while j1 < len(line) and line[j1].isdigit():
                    j1 += 1
                m_i = i - 1 if i > 0 else i
                m_j = j - 1 if j > 0 else j
                checked = False
                for x in (line[m_j:j1 + 1] for line in s[m_i:i + 2]):
                    if checked:
                        break
                    for c in x:
                        if not c.isdigit() and c != '.':
                            part_nos.append(int(line[j:j1]))
                            checked = True
                            break
                j = j1
            else:
                j += 1
    return sum(part_nos)


print(sum_part_nos(inp))
