import sys


def main():
    increases = 0
    last = None
    for line in sys.stdin:
        value = int(line.strip())
        if last is not None and value > last:
            increases += 1
        last = value

    print("-" * 50)
    print(increases)


if __name__ == "__main__":
    main()
