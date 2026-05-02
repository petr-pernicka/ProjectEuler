def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


def choose(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def main():
    GRID_SIDE = 20

    n = GRID_SIDE * 2
    k = GRID_SIDE

    print(choose(n, k))


if __name__ == '__main__':
    main()
