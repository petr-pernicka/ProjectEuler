def letter_to_num(letter: str):
    return ord(letter) - ord('A') + 1


def main():
    with open("22.txt", 'r') as f:
        names = f.readline().split(',')
        names = [name[1:-1] for name in names]
        names = sorted(names)

    sum = 0
    for i, name in enumerate(names):

        n = 0
        for letter in name:
            n += letter_to_num(letter)

        sum += n * (i + 1)

    print(sum)


if __name__ == '__main__':
    main()
