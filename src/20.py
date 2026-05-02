import math


def digit_sum(n: int):
    digits = math.floor(math.log10(n)) + 1

    sum = 0
    for i in range(digits):
        a = n // 10
        sum += n - a * 10
        n = a

    return sum


def factorial(n: int):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


def main():
    print(digit_sum(factorial(100)))


if __name__ == '__main__':
    main()
