N = 100


def generate_fraction_sequence():
    seq = [2, 1]

    k = 2
    for i in range(N - 2):
        if i % 3 == 0:
            seq.append(k)
            k += 2
        else:
            seq.append(1)

    return seq


def main():
    seq = generate_fraction_sequence()
    numer, denom = 1, seq[-1]  # 1 / last in seq

    for x in reversed(seq[:-1]):
        x_common_denom = x * denom
        numer += x_common_denom
        numer, denom = denom, numer

    numer, denom = denom, numer
    print(f"{numer}/{denom}")

    digit_sum = 0
    for d in str(numer):
        digit_sum += int(d)
    print(f"Sum of digits in the numerator of {N}th convergent of continued fraction for e: {digit_sum}")


if __name__ == '__main__':
    main()
