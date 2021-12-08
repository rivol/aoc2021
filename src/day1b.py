import sys


def main():
    measurements = []
    for line in sys.stdin:
        value = int(line.strip())
        measurements.append(value)

    increases = 0
    for i in range(3, len(measurements)):
        value_a = sum(measurements[i - 3 : i])
        value_b = sum(measurements[i - 2 : i + 1])
        if value_b > value_a:
            increases += 1

    print("-" * 50)
    print(increases)


if __name__ == "__main__":
    main()
