import functools
import requests
import os
from dotenv import load_dotenv

load_dotenv()

pinput = requests.get('https://adventofcode.com/2023/day/16/input', cookies={"session": os.getenv("SESSION")}).text
# pinput = r""".|...\....
# |.-.\.....
# .....|-...
# ........|.
# ..........
# .........\
# ..../.\\..
# .-.-/..|..
# .|....-|.\
# ..//.|...."""


class Light:
    def __init__(self, x, y, dx, dy):
        self.x, self.y, self.dx, self.dy = x, y, dx, dy

    def move(self, grid: list[str]) -> list["Light"]:
        x, y, dx, dy = self.x, self.y, self.dx, self.dy
        if (x + dx) >= len(grid[0]) or (x + dx) < 0 or (y + dy) >= len(grid) or (y + dy) < 0:
            return []
        if grid[y + dy][x + dx] == ".":
            self.x += dx
            self.y += dy
            return [self]
        elif grid[y + dy][x + dx] == "/":
            self.x += dx
            self.y += dy
            if dx == 1:
                self.dx, self.dy = 0, -1
            elif dx == -1:
                self.dx, self.dy = 0, 1
            elif dy == 1:
                self.dx, self.dy = -1, 0
            elif dy == -1:
                self.dx, self.dy = 1, 0
            return [self]
        elif grid[y + dy][x + dx] == "\\":
            self.x += dx
            self.y += dy
            if self.dx == 1:
                self.dx, self.dy = 0, 1
            elif self.dx == -1:
                self.dx, self.dy = 0, -1
            elif self.dy == 1:
                self.dx, self.dy = 1, 0
            elif self.dy == -1:
                self.dx, self.dy = -1, 0
            return [self]
        elif grid[y + dy][x + dx] == "-":
            self.x += dx
            self.y += dy
            if dx in (1, -1):
                return [self]
            self.dx = 1
            self.dy = 0
            return [self, Light(self.x, self.y, -1, 0)]
        elif grid[y + dy][x + dx] == "|":
            self.x += dx
            self.y += dy
            if dy in (1, -1):
                return [self]
            self.dx = 0
            self.dy = 1
            return [self, Light(self.x, self.y, 0, -1)]
        return []

    def get_d(self) -> tuple[int, int]:
        return self.dx, self.dy


def main():
    lines = pinput.splitlines()
    encountered = [[set() for _ in range(len(lines[0]))] for _ in range(len(lines))]
    lights = [Light(-1, 0, 1, 0)]
    enlightened = set()
    while lights:
        curr = lights.pop()
        new_lights = curr.move(lines)
        for light in new_lights:
            enlightened.add((light.x, light.y))
            if light.get_d() in encountered[light.y][light.x]:
                continue
            encountered[light.y][light.x].add(light.get_d())
            lights.append(light)
    print(len(enlightened))


if __name__ == "__main__":
    main()
