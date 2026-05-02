import math


def neighbors(node):
    line = math.floor(math.sqrt(2 * node + 1 / 4) - 1 / 2)
    x = (line + 1) * line / 2
    line += 1
    y = (line + 1) * line / 2
    n = node - x + y
    return n, n + 1


def main():
    data = []
    with open("67.txt") as file:
        lines = file.readlines()
        for line in lines:
            arr = line.split()
            for x in arr:
                data.append(int(x))

    print(data)

    distance = [-math.inf] * len(data)
    distance[0] = data[0]
    for v in range(len(data)):
        n1, n2 = neighbors(v)
        n1, n2 = int(n1), int(n2)
        if n1 >= len(data):
            break

        new_dist1 = distance[v] + data[n1]
        if distance[n1] < new_dist1:
            distance[n1] = new_dist1

        new_dist2 = distance[v] + data[n2]
        if distance[n2] < new_dist2:
            distance[n2] = new_dist2

    print(max(distance))


if __name__ == '__main__':
    main()
