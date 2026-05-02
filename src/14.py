def collatz_length(i: int):
    len = 1

    while i != 1:
        if i % 2 == 0:
            i /= 2
        else:
            i = 3 * i + 1
        len += 1

    return len


def main():
    max_len = 0
    max_len_i = 0

    for i in range(4, 1_000_000):
        i_len = collatz_length(i)
        if max_len < i_len:
            max_len = i_len
            max_len_i = i

        if i % 10000 == 0:
            print(i)

    print(f"{max_len_i}: {max_len}")


if __name__ == '__main__':
    main()
