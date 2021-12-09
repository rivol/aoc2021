import sys


def main():
    start_positions = [int(pos) for pos in sys.stdin.read().strip().split(",")]

    print("-" * 50)
    print(f"max: {max(start_positions)}, count: {len(start_positions)}")

    max_x = max(start_positions)

    cheapest = None
    for x in range(0, max_x + 1):
        cost = 0
        for crab_x in start_positions:
            dx = abs(x - crab_x)
            # Moving by dx units cost 1+2+...+dx = dx*(1+dx)/2  (sum of arithmetic sequence)
            cost += dx * (1 + dx) // 2
        print(f"{x=} {cost=}")

        if cheapest is None or cost < cheapest:
            cheapest = cost

    print("-" * 50)
    print(cheapest)


if __name__ == "__main__":
    main()
