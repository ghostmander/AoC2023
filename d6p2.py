import requests
import os
from dotenv import load_dotenv

load_dotenv()
inp = requests.get('https://adventofcode.com/2023/day/6/input', cookies={"session": os.getenv("SESSION")}).text

# inp = """Time:      7  15   30
# Distance:  9  40  200"""


inp = inp.strip('\n').split('\n')
time = int(inp[0].split(':')[1].strip().replace(' ', ''))
distance = int(inp[1].split(':')[1].strip().replace(' ', ''))
d = (time**2 - 4*distance)**0.5
print(abs(round((time-d)/2 - (time+d)/2))-1)
