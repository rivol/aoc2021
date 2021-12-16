import sys
from typing import List, Tuple


def print_grid(map_yx, sep=""):
    for row in map_yx:
        viz = ["." if col is None else str(col) for col in row]
        print(sep.join(viz))


def make_grid(w, h, value) -> List[list]:
    grid = []
    for _ in range(h):
        grid.append([value] * w)
    return grid


def fold_map(map, w: int, h: int, axis: str, coord: int):
    # each fold seems to fold the map exactly in half (i.e both halves are of equal size). we don't handle other cases.
    new_w = w
    new_h = h
    if axis == "x":
        assert coord * 2 + 1 == w
        new_w = coord
    elif axis == "y":
        assert coord * 2 + 1 == h
        new_h = coord
    else:
        raise Exception(f"invalid fold instruction {axis}={coord} for map size {w}x{h}")

    new_map = make_grid(new_w, new_h, None)
    for y in range(new_h):
        for x in range(new_w):
            if axis == "x":
                new_map[y][x] = map[y][x] or map[y][w - x - 1]
            if axis == "y":
                new_map[y][x] = map[y][x] or map[h - y - 1][x]

    return new_map, new_w, new_h


def main():
    points: List[Tuple[int, int]] = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            break
        point = tuple([int(coord) for coord in line.split(",")])
        assert len(point) == 2
        points.append(point)

    # each fold is tuple ala  ('x', 5)
    folds: List[Tuple[str, int]] = []
    for line in sys.stdin:
        instruction = line.split()[2].split("=")
        instruction[1] = int(instruction[1])
        folds.append(tuple(instruction))

    print("-" * 50)
    for point in points:
        print(point)
    for fold_axis, fold_coord in folds:
        print(f"fold: {fold_axis} = {fold_coord}")

    print("-" * 50)
    w = max(p[0] for p in points) + 1
    h = max(p[1] for p in points) + 1
    map = make_grid(w, h, None)
    for x, y in points:
        map[y][x] = 1
    print(f"initial map {w}x{h}:")
    print_grid(map)

    for fold in folds:
        map, w, h = fold_map(map, w, h, fold[0], fold[1])
        print(f"folded map {w}x{h}:")
        print_grid(map)

        # do only a single fold for now
        break

    # counts dots
    dots = 0
    for y in range(h):
        for x in range(w):
            if map[y][x] is not None:
                dots += 1

    print("-" * 50)
    print(dots)


if __name__ == "__main__":
    main()
