import sys


def is_low_point(map, x, y) -> bool:
    # Look at 3x3 area centered on this cell
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                # skip the middle cell
                continue
            if map[y][x] >= map[y + dy][x + dx]:
                return False

    return True


def main():
    # map[y][x]  gives height
    map = []
    for line in sys.stdin.readlines():
        line = line.strip()
        map.append([int(char) for char in line])

    # pad the map with high values, so that we can look at adjacent cells without running into edges
    map_w = len(map[0])
    map.insert(0, [9] * (map_w + 2))
    for row in map[1:]:
        row.insert(0, 9)
        row.append(9)
    map.append([9] * (map_w + 2))

    # display padded map
    print("-" * 50)
    for row in map:
        print(row)

    low_point_heights = []
    for y in range(1, len(map) - 1):
        for x in range(1, 1 + map_w):
            if is_low_point(map, x, y):
                low_point_heights.append(map[y][x])

    risk_levels = [1 + h for h in low_point_heights]

    print("-" * 50)
    print(sum(risk_levels))


if __name__ == "__main__":
    main()
