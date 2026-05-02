import time

"""
Hledáme n, kdy tf(n) je malé => hledáme hodně složená čísla.
Ok, je to 2 * 3 * 5 * 7 * 11 * 13 * 17 (největší číslo složené
z prvních prvočísel)
"""


def gcd1(a: int, b: int) -> int:
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def gcd2(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def totient_function(n: int) -> int:
    count = 0

    for i in range(1, n):
        if gcd1(n, i) == 1:
            count += 1

    return count


def main():
    MAX = 100
    max_n = -1
    max_ratio = 1

    for n in range(2, MAX + 1):
        print(n)
        tf = totient_function(n)
        ratio = n / tf
        if ratio > max_ratio:
            max_ratio = ratio
            max_n = n

    print(f"N with maximum ratio is: {max_n} with ratio {max_ratio}")



if __name__ == '__main__':
    n = 2 * 3 * 5 * 7 * 11 * 13 * 17
    print(n / totient_function(n))
    exit(0)

    t = time.time()
    main()
    print(f"Done in {time.time() - t:.2f}s")
