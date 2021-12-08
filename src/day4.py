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
    drawn = [int(value) for value in sys.stdin.readline().strip().split(",")]

    boards = []
    while True:
        line = sys.stdin.readline()
        if line == "":
            break
        assert line == "\n"

        board = []
        while len(board) < 5:
            line = sys.stdin.readline()
            nums = [int(value) for value in line.split()]
            assert len(nums) == 5
            board.append(nums)

        boards.append(board)

    results = []
    for board in boards:
        n, result = play_board(board, drawn)
        print(n, result)
        results.append((n, result))

    results = sorted(results)

    print("-" * 50)
    print(results[0][1])


if __name__ == "__main__":
    main()
