import sys
from collections import Counter, defaultdict
from typing import Dict


def run_step(occurrences: Dict[str, int], rules: Dict[str, str]) -> Dict[str, int]:
    result = defaultdict(int)
    for pair, count in occurrences.items():
        insertion = rules.get(pair)

        if insertion is None:
            result[pair] += count
        else:
            result[pair[0] + insertion] += count
            result[insertion + pair[1]] += count

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

    # Simulating the whole sequence of letters is prohibitively expensive for 40 steps.
    # Instead, just keep track of how many of each pairs of letters we have, and simulate those.
    occurrences = defaultdict(int)
    # Hack: add special character to the end of the polymer string to make counting easier
    polymer += "-"
    for i in range(1, len(polymer)):
        pair = polymer[i - 1 : i + 1]
        occurrences[pair] += 1

    for step in range(40):
        occurrences = run_step(occurrences, rules)
        print(f"after step {step+1}: len={sum(occurrences.values())} {occurrences=}")

    counter = Counter()
    for pair, count in occurrences.items():
        # Avoid double counting by only looking at the first char. The hack above makes it work.
        counter[pair[0]] += count
    print(counter)
    # counts is list of  (item, count)  tuples
    counts = counter.most_common()

    print("-" * 50)
    print(counts[0][1] - counts[-1][1])


if __name__ == "__main__":
    main()
