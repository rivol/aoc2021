import sys
from typing import List, Optional, Tuple


class MatchException(Exception):
    pass


def get_score(board: List[List[int]], matches: List[List[Optional[int]]], last_drawn: int) -> int:
    unmarked_nums = []
    for i in range(5):
        for j in range(5):
            if matches[i][j] is None:
                unmarked_nums.append(board[i][j])

    return sum(unmarked_nums) * last_drawn


def play_board(board: List[List[int]], drawn: List[int]) -> Tuple[Optional[int], Optional[int]]:
    matches = []
    for i in range(5):
        matches.append([None] * 5)
    print(matches)

    for x, num in enumerate(drawn):
        try:
            for i, row in enumerate(board):
                for j, col in enumerate(row):
                    if col == num:
                        matches[i][j] = num
                        # Stupid flow control
                        raise MatchException()
        except MatchException:
            # Check if we've won
            for i in range(5):
                if all(matches[i]):
                    print(num, "row", matches[i], matches)
                    return x, get_score(board, matches, num)
            for j in range(5):
                values = [row[j] for row in matches]
                if all(values):
                    print(num, "col", values, matches)
                    return x, get_score(board, matches, num)

    return None, None


def main():
    data = []
    for line in sys.stdin:
        value = line.strip()
        # line is ((x1, y1), (x2, y2))
        line = [[int(value) for value in pos.split(",")] for pos in value.split(" -> ")]
        data.append(line)

    print("-" * 50)

    # Figure out the map size
    map_w: int = max(pos[0] for line in data for pos in line) + 1
    map_h: int = max(pos[1] for line in data for pos in line) + 1
    print(f"{map_w=} {map_h=}")

    # map[x][y] is number of vents at that pos
    map = []
    for x in range(map_w):
        map.append([0] * map_h)
    # "paint" the map
    for line in data:
        dx = line[1][0] - line[0][0]
        dy = line[1][1] - line[0][1]

        dist = max(abs(dx), abs(dy))

        step_x = dx // abs(dx) if dx else 0
        step_y = dy // abs(dy) if dy else 0
        for i in range(dist + 1):
            x = line[0][0] + step_x * i
            y = line[0][1] + step_y * i
            map[x][y] += 1

    dangers = 0
    for y in range(map_h):
        for x in range(map_w):
            vents = map[x][y]
            print(str(vents) if vents else ".", end="")
            if vents > 1:
                dangers += 1

        print()

    print("-" * 50)
    print(dangers)


if __name__ == "__main__":
    main()
