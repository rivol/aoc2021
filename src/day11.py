import sys
from collections import deque


def print_grid(map_yx, sep=""):
    for row in map_yx:
        viz = ["." if col is None else str(col) for col in row]
        print(sep.join(viz))


def pad_map(map, value):
    map_w = len(map[0])
    map.insert(0, [value] * (map_w + 2))
    for row in map[1:]:
        row.insert(0, value)
        row.append(value)
    map.append([value] * (map_w + 2))


def sim(map) -> int:
    # queue of octopuses that have flashed and need to be processed
    flashed = []
    flash_q = deque()
    # add 1 to all
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] is None or map[y][x] > 9:
                continue

            if map[y][x] == 9:
                flash_q.append((x, y))
            map[y][x] += 1

    # process flashes
    while flash_q:
        flashx, flashy = flash_q.popleft()
        print(f"flash at ({flashx} {flashy})")
        flashed.append((flashx, flashy))
        # process 3x3 area around the flash. don't bother skipping the center part, it won't matter
        for x in range(flashx - 1, flashx + 2):
            for y in range(flashy - 1, flashy + 2):
                if map[y][x] is None:
                    continue
                # it'll flash if it's exactly 9 ATM
                if map[y][x] == 9:
                    flash_q.append((x, y))
                map[y][x] += 1

    # reset all flashed cells to 0
    for x, y in flashed:
        map[y][x] = 0

    # return num of flashes
    return len(flashed)


def main():
    map = [[int(char) for char in line.strip()] for line in sys.stdin.readlines()]
    print("-" * 50)

    pad_map(map, None)
    print_grid(map)

    total_flashes = 0
    for step in range(100):
        print("-" * 50)
        print(f"Step {step}")

        flashes = sim(map)
        total_flashes += flashes

        print_grid(map)
        print(f"Total flashes {total_flashes}, this step: {flashes}")

    print("-" * 50)
    print(total_flashes)


if __name__ == "__main__":
    main()
