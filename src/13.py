
def parse(path):
    nums = []
    with open(path, 'r') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            nums.append(int(line))
    return nums


def main():
    sum = 0

    for i in parse('13.txt'):
        sum += i

    print(sum)


if __name__ == '__main__':
    main()
