import sys


def main():
    depth = 0
    distance = 0

    for line in sys.stdin:
        command, value = line.split()
        value = int(value)

        if command == "forward":
            distance += value
        elif command == "down":
            depth += value
        elif command == "up":
            depth -= value
        else:
            raise RuntimeError(f"Invalid command: '{command}'")

    print("-" * 50)
    print(f"{distance=} {depth=}")

    print("-" * 50)
    print(distance * depth)


if __name__ == "__main__":
    main()
