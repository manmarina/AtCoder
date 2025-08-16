import itertools

K, S = map(int, input().split())


def sum_of_3_integers(limit, total):
    three_integers = itertools.product(
        range(limit + 1), repeat=3)

    count = 0
    for three_integer in three_integers:
        if sum(three_integer) == total:
            count += 1

    return count


print(sum_of_3_integers(K, S))
