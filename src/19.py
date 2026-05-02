def sundays_on_first(year: int, jan1: int):
    if year % 4 == 0:
        february = 29
        if year % 100 == 0:
            february = 28
        if year % 400 == 0:
            february = 29
    else:
        february = 28

    months = [31, february, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    count = 0
    day1 = jan1
    for month in months:
        if day1 == 6:
            count += 1

        day1 = (day1 + month) % 7

    return count, day1


def main():
    jan1 = 1  # 1 Jan 1901 is Tuesday

    count = 0
    for year in range(1901, 2001):
        c, j1, = sundays_on_first(year, jan1)
        count += c
        jan1 = j1

    print(count)


if __name__ == '__main__':
    main()
