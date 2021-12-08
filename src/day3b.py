import sys
from collections import Counter
from typing import List


def get_most_common(bits: List[str]) -> str:
    counts = Counter(bits)
    # not using  counts.most_common(1)...  because equal counts need special handling
    if counts["1"] >= counts["0"]:
        return "1"
    else:
        return "0"


def search(data: List[str], use_most_common: bool) -> str:
    for i in range(len(data[0])):
        bits = [value[i] for value in data]
        most_common = get_most_common(bits)
        target = most_common if use_most_common else ("1" if most_common == "0" else "0")

        data = [value for value in data if value[i] == target]

        if len(data) == 1:
            return data[0]


def main():
    data = []
    for line in sys.stdin:
        value = line.strip()
        data.append(value)

    # Sanity check that all values have same length
    for value in data:
        assert len(value) == len(data[0])

    oxygen = search(data, use_most_common=True)
    co2 = search(data, use_most_common=False)

    # Convert to integers
    oxygen = int(oxygen, 2)
    co2 = int(co2, 2)

    print("-" * 50)
    print(f"{oxygen=} {co2=}")

    print("-" * 50)
    print(oxygen * co2)


if __name__ == "__main__":
    main()
