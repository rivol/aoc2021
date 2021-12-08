import sys
from collections import Counter


def main():
    data = []
    for line in sys.stdin:
        value = line.strip()
        data.append(value)

    # Sanity check that all values have same length
    for value in data:
        assert len(value) == len(data[0])

    gamma_rate = ""
    epsilon_rate = ""
    for i in range(len(data[0])):
        bits = [value[i] for value in data]
        counts = Counter(bits)
        if counts["0"] > counts["1"]:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    # Epsilon actually seems to be exact inverse of gamma, in binary...

    # Convert to integers
    gamma_rate = int(gamma_rate, 2)
    epsilon_rate = int(epsilon_rate, 2)

    print("-" * 50)
    print(f"{gamma_rate=} {epsilon_rate=}")

    print("-" * 50)
    print(gamma_rate * epsilon_rate)


if __name__ == "__main__":
    main()
