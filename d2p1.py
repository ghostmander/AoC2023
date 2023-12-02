import requests
import os
from dotenv import load_dotenv
import re

load_dotenv()
inp = requests.get('https://adventofcode.com/2023/day/2/input', cookies={"session": os.getenv("SESSION")}).text


def process_game(s: str, lims: tuple = (12, 13, 14)) -> int:
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
    if reds > lims[0] or greens > lims[1] or blues > lims[2]:
        # print(f"Game {game_id} is invalid")
        return 0
    return int(game_id)


print(sum(process_game(line) for line in inp.split('\n')))
