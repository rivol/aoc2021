import sys

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


class CorruptionException(Exception):
    def __init__(self, expression: str, pos: int, expected: str) -> None:
        super().__init__()
        self.expression = expression
        self.pos = pos
        self.expected = expected


class IncompleteException(Exception):
    pass


def parse(expression: str, pos=0) -> int:
    while pos < len(expression) and expression[pos] in OPENERS:
        # parse subexpression
        # consume opener
        opener = expression[pos]
        pos += 1
        # consume nested expressions
        pos = parse(expression, pos)

        # consume closer
        if expression[pos] != OPENER_TO_CLOSER[opener]:
            raise CorruptionException(expression, pos, expected=OPENER_TO_CLOSER[opener])
        pos += 1

    if pos >= len(expression):
        raise IncompleteException()

    return pos


def main():
    lines = [line.strip() for line in sys.stdin.readlines()]
    print("-" * 50)

    score = 0
    for line in lines:
        try:
            parse(line)
        except CorruptionException as e:
            subscore = INVALID_CHAR_SCORES[e.expression[e.pos]]
            print(
                f"corrupted: {line}   (invalid_char: {e.expression[e.pos]} at pos {e.pos}, expected {e.expected}, score: {subscore})"
            )
            score += subscore
            continue
        except IncompleteException as e:
            print(f"incomplete: {line}")
            continue
        print(f"good: {line}")

    print("-" * 50)
    print(score)


if __name__ == "__main__":
    main()
