import sys
from collections import defaultdict


def sim(state: dict, days: int) -> int:
    for day in range(days):
        new_state = {i: 0 for i in range(8 + 1)}

        for i in range(1, 8 + 1):
            new_state[i - 1] = state[i]
        new_state[8] += state[0]
        new_state[6] += state[0]

        state = new_state

        total = sum(state.values())
        print(f"after {day+1} days: {total=}")

    return sum(state.values())


def main():
    fishies = [int(fish) for fish in sys.stdin.read().strip().split(",")]
    print("-" * 50)

    # Model the fish by keeping track how many have N days left until reproducing, i.e don't track each one separately.
    state = defaultdict(int)
    for days in fishies:
        state[days] += 1

    fish_after_80 = sim(state, 80)
    # this double-prints the counts for the first 80 days :shrug:
    fish_after_256 = sim(state, 256)

    print("-" * 50)
    print(fish_after_80)
    print("-" * 50)
    print(fish_after_256)


if __name__ == "__main__":
    main()
