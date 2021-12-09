import sys
from collections import defaultdict


def main():
    fishies = [int(fish) for fish in sys.stdin.read().strip().split(",")]
    print("-" * 50)

    # Model the fish by keeping track how many have N days left until reproducing, i.e don't track each one separately.
    state = defaultdict(int)
    for days in fishies:
        state[days] += 1

    for day in range(80):
        new_state = {i: 0 for i in range(8 + 1)}

        for i in range(1, 8 + 1):
            new_state[i - 1] = state[i]
        new_state[8] += state[0]
        new_state[6] += state[0]

        state = new_state

        total = sum(state.values())
        print(f"after {day+1} days: {total=}")

    print("-" * 50)
    print(sum(state.values()))


if __name__ == "__main__":
    main()
