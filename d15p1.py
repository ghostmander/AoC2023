import requests
import os
from dotenv import load_dotenv

load_dotenv()
pinput = requests.get('https://adventofcode.com/2023/day/15/input', cookies={"session": os.getenv("SESSION")}).text


def get_hash(s: str) -> int:
    curr_hash = 0
    for _c in s:
        curr_hash = (curr_hash + ord(_c)) * 17 % 256
    return curr_hash


print(sum(get_hash(s.strip('\n')) for s in pinput.split(',')))
