import requests
import os
from dotenv import load_dotenv
from collections import defaultdict

load_dotenv()
inp = requests.get('https://adventofcode.com/2023/day/5/input', cookies={"session": os.getenv("SESSION")}).text

# inp = """seeds: 79 14 55 13
#
# seed-to-soil map:
# 50 98 2
# 52 50 48
#
# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15
#
# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4
#
# water-to-light map:
# 88 18 7
# 18 25 70
#
# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13
#
# temperature-to-humidity map:
# 0 69 1
# 1 0 69
#
# humidity-to-location map:
# 60 56 37
# 56 93 4"""


def input_processor(s: str) -> tuple[list, dict]:
    seeds = []
    processed = {
        "seed_to_soil_map": {},
        "soil_to_fertilizer_map": {},
        "fertilizer_to_water_map": {},
        "water_to_light_map": {},
        "light_to_temperature_map": {},
        "temperature_to_humidity_map": {},
        "humidity_to_location_map": {}
    }
    key = None

    s = s.strip('\n').split('\n')
    for line in s:
        if line == '':
            continue
        elif line.startswith('seeds:'):
            seeds = [*map(int, line.split(':')[1].strip().split(' '))]
            continue
        elif line.startswith('seed-to-soil map:'):
            key = "seed_to_soil_map"
            continue
        elif line.startswith('soil-to-fertilizer map:'):
            key = "soil_to_fertilizer_map"
            continue
        elif line.startswith('fertilizer-to-water map:'):
            key = "fertilizer_to_water_map"
            continue
        elif line.startswith('water-to-light map:'):
            key = "water_to_light_map"
            continue
        elif line.startswith('light-to-temperature map:'):
            key = "light_to_temperature_map"
            continue
        elif line.startswith('temperature-to-humidity map:'):
            key = "temperature_to_humidity_map"
            continue
        elif line.startswith('humidity-to-location map:'):
            key = "humidity_to_location_map"
            continue

        s, d, r = map(int, line.split())
        processed[key][(d, d + r)] = s - d
    return seeds, processed


def get_location(seed_value, lookup_maps):
    def get_mapped_value(lookup_map: dict, value: int) -> int:
        for k, v in lookup_map.items():
            if k[0] <= value < k[1]:
                return v + value
        return value

    soil = get_mapped_value(lookup_maps["seed_to_soil_map"], seed_value)
    fertilizer = get_mapped_value(lookup_maps["soil_to_fertilizer_map"], soil)
    water = get_mapped_value(lookup_maps["fertilizer_to_water_map"], fertilizer)
    light = get_mapped_value(lookup_maps["water_to_light_map"], water)
    temperature = get_mapped_value(lookup_maps["light_to_temperature_map"], light)
    humidity = get_mapped_value(lookup_maps["temperature_to_humidity_map"], temperature)
    location = get_mapped_value(lookup_maps["humidity_to_location_map"], humidity)
    return location


planting_seeds, seed_map = input_processor(inp)
min_location = float('inf')
for seed in planting_seeds:
    min_location = min(min_location, get_location(seed, seed_map))
print(min_location)
