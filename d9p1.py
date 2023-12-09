import re

import requests
import os
from dotenv import load_dotenv

load_dotenv()
pinput = requests.get('https://adventofcode.com/2023/day/9/input', cookies={"session": os.getenv("SESSION")}).text
# pinput = """0 3 6 9 12 15
# 1 3 6 10 15 21
# 10 13 16 21 30 45
# """


def extrapolate(line: str) -> int:
    nums = [[int(num) for num in line.split()]]
    try:
        while len(set(nums[-1])) > 1:
            nums.append([nums[-1][i] - nums[-1][i-1] for i in range(1, len(nums[-1]))] or [0])
        return sum(x[-1] for x in nums)
    except IndexError:
        print(line, nums)
        return 0


def main(inp: str):
    print(*(extrapolate(line) for line in inp.splitlines()))
    print(sum(extrapolate(line) for line in inp.splitlines()))


main(pinput)
