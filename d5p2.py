import requests
import os
from dotenv import load_dotenv
import time

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


def input_processor_reverse(s: str) -> tuple[list, dict]:
    seeds = []
    processed = {
        "location_to_humidity_map": {},
        "humidity_to_temperature_map": {},
        "temperature_to_light_map": {},
        "light_to_water_map": {},
        "fertilizer_to_soil_map": {},
        "water_to_fertilizer_map": {},
        "soil_to_seed_map": {},
    }
    key = None

    s = s.strip('\n').split('\n')
    for line in s:
        if line == '':
            continue
        elif line.startswith('seeds:'):
            seeds = [*map(int, line.split(':')[1].strip().split(' '))]
            seeds = [(s, s + r) for s, r in [seeds[x:x + 2] for x in range(0, len(seeds), 2)]]
            continue
        elif line.startswith('seed-to-soil map:'):
            key = "soil_to_seed_map"
            continue
        elif line.startswith('soil-to-fertilizer map:'):
            key = "fertilizer_to_soil_map"
            continue
        elif line.startswith('fertilizer-to-water map:'):
            key = "water_to_fertilizer_map"
            continue
        elif line.startswith('water-to-light map:'):
            key = "light_to_water_map"
            continue
        elif line.startswith('light-to-temperature map:'):
            key = "temperature_to_light_map"
            continue
        elif line.startswith('temperature-to-humidity map:'):
            key = "humidity_to_temperature_map"
            continue
        elif line.startswith('humidity-to-location map:'):
            key = "location_to_humidity_map"
            continue

        s, d, r = map(int, line.split())
        processed[key][(s, s + r)] = d - s
    return seeds, processed


def get_seed(location_value, lookup_maps):
    def get_mapped_value(lookup_map: dict, value: int) -> int:
        for k, v in lookup_map.items():
            if k[0] <= value < k[1]:
                return v + value
        return value

    humidity = get_mapped_value(lookup_maps["location_to_humidity_map"], location_value)
    temperature = get_mapped_value(lookup_maps["humidity_to_temperature_map"], humidity)
    light = get_mapped_value(lookup_maps["temperature_to_light_map"], temperature)
    water = get_mapped_value(lookup_maps["light_to_water_map"], light)
    fertilizer = get_mapped_value(lookup_maps["water_to_fertilizer_map"], water)
    soil = get_mapped_value(lookup_maps["fertilizer_to_soil_map"], fertilizer)
    return get_mapped_value(lookup_maps["soil_to_seed_map"], soil)


def check_if_seed_exists(seed_ranges, seed_value):
    for low, high in seed_ranges:
        if low <= seed_value < high:
            return True
    return False


st = time.time()
planting_seeds, seed_map = input_processor_reverse(inp)
pt = time.time()
print(f"Processing Time: {pt - st}")
loc = 81_900_000
while True:
    if loc % 10_000_000 == 0:
        print(f"Reached {loc:,d} [Time: {time.time() - pt}]")
    seed = get_seed(loc, seed_map)
    if check_if_seed_exists(planting_seeds, seed):
        break
    loc += 1
print(f"Min Location Time: {time.time() - pt}")
print(f"Total Time: {time.time() - st}")
print(loc)
