import sys
from queue import PriorityQueue
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


def pad_map(map, value):
    map_w = len(map[0])
    map.insert(0, [value] * (map_w + 2))
    for row in map[1:]:
        row.insert(0, value)
        row.append(value)
    map.append([value] * (map_w + 2))


def dijkstra(map, w, h):
    # writing Dijkstra from scratch on an airplane is an interesting challenge :-P
    totals = make_grid(w, h, None)
    totals[1][1] = 0

    # items are  (cost, x, y)  tuples
    q = PriorityQueue()
    q.put((0, 1, 1))
    while not q.empty():
        cost, x, y = q.get()
        neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
        for newx, newy in neighbors:
            if map[newy][newx] is None:
                continue
            new_cost = cost + map[newy][newx]
            if totals[newy][newx] is None or totals[newy][newx] > new_cost:
                print(f"  D: step: ({x},{y}) = {new_cost} (from {totals[newy][newx]}")
                totals[newy][newx] = new_cost
                q.put((new_cost, newx, newy))

    print_grid(totals, " ")
    return totals[h - 2][w - 2]


def main():
    map = [[int(char) for char in line.strip()] for line in sys.stdin.readlines()]
    print("-" * 50)

    # Resize map
    w = len(map[0])
    h = len(map)
    big_map = make_grid(w * 5, h * 5, 0)
    for y in range(w):
        for x in range(h):
            for xm in range(0, 5):
                for ym in range(0, 5):
                    risk = map[y][x] + xm + ym
                    if risk > 9:
                        risk -= 9
                    big_map[ym * h + y][xm * w + x] = risk
    map = big_map

    pad_map(map, None)
    w = len(map[0])
    h = len(map)
    print(f"initial map {w}x{h}:")
    print_grid(map)

    print("-" * 50)
    cost = dijkstra(map, w, h)
    print("-" * 50)

    print(cost)


if __name__ == "__main__":
    main()
