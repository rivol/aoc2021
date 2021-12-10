import sys
from statistics import median

OPENER_TO_CLOSER = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}
OPENERS = list(OPENER_TO_CLOSER.keys())
INVALID_CHAR_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
FIX_CHAR_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


class CorruptionException(Exception):
    def __init__(self, expression: str, pos: int, expected: str) -> None:
        super().__init__()
        self.expression = expression
        self.pos = pos
        self.expected = expected


class IncompleteException(Exception):
    def __init__(self, fix: str) -> None:
        super().__init__()
        self.fix = fix


def parse(expression: str, pos=0) -> int:
    while pos < len(expression) and expression[pos] in OPENERS:
        # parse subexpression
        # consume opener
        opener = expression[pos]
        pos += 1
        # consume nested expressions
        try:
            pos = parse(expression, pos)
        except IncompleteException as e:
            raise IncompleteException(fix=e.fix + OPENER_TO_CLOSER[opener])

        # consume closer
        if expression[pos] != OPENER_TO_CLOSER[opener]:
            raise CorruptionException(expression, pos, expected=OPENER_TO_CLOSER[opener])
        pos += 1

    if pos >= len(expression):
        raise IncompleteException(fix="")

    return pos


def main():
    lines = [line.strip() for line in sys.stdin.readlines()]
    print("-" * 50)

    corruption_score = 0
    fix_scores = []
    for line in lines:
        try:
            parse(line)
        except CorruptionException as e:
            subscore = INVALID_CHAR_SCORES[e.expression[e.pos]]
            print(
                f"corrupted: {line}   (invalid_char: {e.expression[e.pos]} at pos {e.pos}, expected {e.expected}, score: {subscore})"
            )
            corruption_score += subscore
            continue
        except IncompleteException as e:
            subscore = 0
            for char in e.fix:
                subscore = subscore * 5 + FIX_CHAR_SCORES[char]
            fix_scores.append(subscore)
            print(f"incomplete: {line}; fix: {e.fix}, score {subscore}")
            continue
        print(f"good: {line}")

    print("-" * 50)
    print(corruption_score)
    print("-" * 50)
    print(median(fix_scores))


if __name__ == "__main__":
    main()
