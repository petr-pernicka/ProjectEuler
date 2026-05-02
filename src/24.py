import math, time

N = 1_000_000


def nth_permutation(set: list, n: int):
    set = set.copy()
    size = len(set)

    permutation = []
    floor = 0
    for steps_num in range(size, 0, -1):
        step = math.factorial(steps_num - 1)

        for i in range(steps_num):
            floor1, ceil1 = floor + i * step, floor + (i + 1) * step

            if floor1 <= n < ceil1:
                permutation.append(set[i])
                set.remove(set[i])
                floor = floor1
                break

    return permutation


def main():
    set = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    p = nth_permutation(set, N - 1)
    print(p)


if __name__ == '__main__':
    t = time.time()
    main()
    print(f"Done in {time.time() - t:.2f}s")
