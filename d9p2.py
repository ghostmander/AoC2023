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
        while any(nums[-1]):
            nums.append([nums[-1][i] - nums[-1][i-1] for i in range(1, len(nums[-1]))] or [0])
        prev = 0
        for i in range(len(nums) - 1, -1, -1):
            prev = nums[i][0] - prev
        return prev
    except IndexError:
        print(line, nums)
        return 0


def main(inp: str):
    print(*(extrapolate(line) for line in inp.splitlines()))
    print(sum(extrapolate(line) for line in inp.splitlines()))


main(pinput)
