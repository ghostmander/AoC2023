import requests
import os
from dotenv import load_dotenv
import re

load_dotenv()
inp = requests.get('https://adventofcode.com/2023/day/2/input', cookies={"session": os.getenv("SESSION")}).text
# inp="""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
# """


def process_game(s: str) -> int:
    if not s:
        return 0
    game_id, game = re.match(r"Game (?P<game_id>\d+): (?P<game>.+)", s).groups()
    games = game.split('; ')
    reds, greens, blues = 0, 0, 0
    for g in games:
        blue = re.search(r"(\d+) blue", g)
        if blue and int(blue.group(1)) > blues:
            blues = int(blue.group(1))
        red = re.search(r"(\d+) red", g)
        if red and int(red.group(1)) > reds:
            reds = int(red.group(1))
        green = re.search(r"(\d+) green", g)
        if green and int(green.group(1)) > greens:
            greens = int(green.group(1))
    return reds * greens * blues


print(sum(process_game(line) for line in inp.split('\n')))
