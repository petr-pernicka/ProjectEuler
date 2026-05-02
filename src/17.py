length = {0: 0,
          1: len("one"),
          2: len("two"),
          3: len("three"),
          4: len("four"),
          5: len("five"),
          6: len("six"),
          7: len("seven"),
          8: len("eight"),
          9: len("nine"),
          10: len("ten"),
          11: len("eleven"),
          12: len("twelve"),
          13: len("thirteen"),
          14: len("fourteen"),
          15: len("fifteen"),
          16: len("sixteen"),
          17: len("seventeen"),
          18: len("eighteen"),
          19: len("nineteen"),
          20: len("twenty"),
          30: len("thirty"),
          40: len("forty"),
          50: len("fifty"),
          60: len("sixty"),
          70: len("seventy"),
          80: len("eighty"),
          90: len("ninety")}


def num_len(num: int):
    if num < 20:
        return length[num]
    if num < 100:
        ten = num - num % 10
        return length[ten] + num_len(num % 10)
    if num < 1000:
        hundred = (num - (num % 100)) / 100
        if num % 100 == 0:
            return length[hundred] + 7

        return length[hundred] + 10 + num_len(num % 100)


def main():
    len = 0
    for i in range(1, 1000):
        len += num_len(i)
    len += 11
    print(len)


if __name__ == '__main__':
    main()
