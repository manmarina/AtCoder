import math

N, D = map(int, input().split())
X = []
for i in range(N):
    X.append(list(map(int, input().split())))


def calc_distance(start, to, dimension, coord):
    temp = 0
    for i in range(dimension):
        temp += abs(coord[start][i] - coord[to][i]) ** 2
    distance = math.sqrt(temp)
    return distance


def count_integer(number, dimension, coord):
    count = 0
    for i in range(number - 1):
        for j in range(i + 1, number):
            distance = calc_distance(i, j, dimension, coord)
            if distance.is_integer():
                count += 1

    return count


print(count_integer(N, D, X))
