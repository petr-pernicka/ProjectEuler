from math import sqrt


def sum_of_natural_numbers(n):
    return n * (n + 1) // 2


def num_of_divisors(n):
    count = 0

    ceil = int(sqrt(n)) + 1
    for i in range(1, ceil):
        if n % i == 0:

            if n / i == i:
                count += 1
            else:
                count += 2

    return count


def main():
    floor = 500

    i = 1
    while True:
        trig_num = sum_of_natural_numbers(i)
        n = num_of_divisors(trig_num)
        if n > floor:
            print(trig_num)
            break
        i += 1


if __name__ == '__main__':
    main()
