import sys
from collections import Counter
from typing import Dict


def run_step(polymer: str, rules: Dict[str, str]) -> str:
    result = polymer[0]
    for i in range(1, len(polymer)):
        insertion = rules.get(polymer[i - 1 : i + 1])
        if insertion is not None:
            result += insertion
        result += polymer[i]

    return result


def main():
    polymer = sys.stdin.readline().strip()

    # Maps pattern to insertion char, e.g "CH": "B"
    rules: Dict[str, str] = {}
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue

        pattern, insertion = line.split(" -> ")
        assert pattern not in rules
        rules[pattern] = insertion

    print("-" * 50)
    print(f"{polymer=}")
    for pattern, insertion in rules:
        print(f"rule: {pattern} -> {insertion}")

    for step in range(10):
        polymer = run_step(polymer, rules)
        print(f"after step {step+1}: len={len(polymer)} {polymer=}")

    # counts is list of  (item, count)  tuples
    counts = Counter(polymer).most_common()

    print("-" * 50)
    print(counts[0][1] - counts[-1][1])


if __name__ == "__main__":
    main()
