import time


N = 100_000
K = 5


def digit_count(n: int):
    counts = list(0 for _ in range(10))

    for s in str(n):
        digit = int(s)
        counts[digit] += 1

    return tuple(counts)


def main():
    cubes = []
    for n in range(100_000):
        cubes.append(n * n * n)

    dict = {}
    for cube in cubes:
        key = digit_count(cube)

        if key not in dict:
            dict[key] = []
        dict[key].append(cube)

    for k, v in dict.items():
        if len(v) == K:
            print(k, min(*v), v)


if __name__ == '__main__':
    # print(digit_count(155))
    # exit(0)

    t1 = time.time()
    main()
    t2 = time.time()
    print(f"{t2 - t1} s")
