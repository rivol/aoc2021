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


def print_grid(map_yx):
    for row in map_yx:
        for col in row:
            print("." if col is None else col, end="")
        print()


def flood(basins, map, source, index) -> int:
    q = [source]
    seen = set()
    size = 0
    while q:
        x, y = q.pop(0)
        if (x, y) in seen:
            continue
        seen.add((x, y))
        basins[y][x] = index
        size += 1

        h = map[y][x]
        if map[y][x - 1] != 9 and map[y][x - 1] > h:
            q.append((x - 1, y))
        if map[y][x + 1] != 9 and map[y][x + 1] > h:
            q.append((x + 1, y))
        if map[y - 1][x] != 9 and map[y - 1][x] > h:
            q.append((x, y - 1))
        if map[y + 1][x] != 9 and map[y + 1][x] > h:
            q.append((x, y + 1))

    return size


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
    print_grid(map)

    low_point_heights = []
    # (x, y) tuple for each low point
    low_points = []
    for y in range(1, len(map) - 1):
        for x in range(1, 1 + map_w):
            if is_low_point(map, x, y):
                low_points.append((x, y))
                low_point_heights.append(map[y][x])

    risk_levels = [1 + h for h in low_point_heights]

    # Flood-fill the basins
    print("-" * 50)
    basins = []
    for _ in range(len(map)):
        basins.append([None] * len(map[0]))
    basin_sizes = []
    for i, low_point in enumerate(low_points):
        size = flood(basins, map, low_point, i)
        basin_sizes.append(size)

    print_grid(basins)
    print(f"{basin_sizes}")

    basin_sizes_sorted = sorted(basin_sizes, reverse=True)

    print("-" * 50)
    print(sum(risk_levels))
    print("-" * 50)
    print(basin_sizes_sorted[0] * basin_sizes_sorted[1] * basin_sizes_sorted[2])


if __name__ == "__main__":
    main()
