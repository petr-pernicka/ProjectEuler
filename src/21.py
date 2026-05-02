import time


def sum_of_divisors(n: int) -> int:
    sum = 0

    for i in range(1, n // 2 + 1):
        if n / i == n // i:
            sum += i

    return sum


def is_amicable(a: int) -> bool:
    b = sum_of_divisors(a)
    if a == b:
        return False

    return a == sum_of_divisors(b)


def main():
    UPPER = 10_000
    sum = 0

    for i in range(1, UPPER):
        if is_amicable(i):
            sum += i

    print(f"Sum of all amicable numbers under {UPPER} is: {sum}")


if __name__ == '__main__':
    t = time.time()
    main()
    print(f"Done in {time.time() - t:.2f}s")
