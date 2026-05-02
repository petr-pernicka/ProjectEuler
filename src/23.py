import time
from math import sqrt

MAX = 28123  # numbers greater than this can be written as sum of two abundant numbers


def is_abundant(n: int):
    divisors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)

    return sum(divisors) > n


def is_abundant2(n: int):
    divisors = [1]

    for i in range(2, n):
        if n % i == 0:
            if sqrt(n) == n / i:
                divisors.append(i)
                break

            if sqrt(n) > n / i:
                break

            divisors.append(i)
            divisors.append(n // i)

    return sum(divisors) > n


def main():
    abundant_numbers = set()
    for n in range(1, MAX + 1):
        if is_abundant2(n):
            abundant_numbers.add(n)

    sum = 0
    for n in range(1, MAX + 1):
        for an1 in abundant_numbers:
            an2 = n - an1
            if an2 in abundant_numbers:
                break
        else:
            sum += n

    print(sum)


if __name__ == '__main__':
    t = time.time()
    main()
    print(f"Done in {time.time() - t:.2f}s")
