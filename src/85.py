def rectangles_in_grid(n, m):
    return m * (m + 1) * n * (n + 1) / 4


def main():
    RECTANGLES = 2_000_000
    n = 0
    m = 0
    solution = 0

    for i in range(1, RECTANGLES):
        for j in range(1, RECTANGLES):
            rentangles_ij = rectangles_in_grid(i, j)

            if abs(RECTANGLES - rentangles_ij) < abs(RECTANGLES - solution):
                solution = rentangles_ij
                n = i
                m = j

            if rentangles_ij > RECTANGLES:
                break

    print(f"{n}x{m}: {solution}")


if __name__ == '__main__':
    main()
