N, A, B = map(int, input().split())


def calc_sum(num):
    return sum(map(int, str(num)))


# total = 0
# for i in range(1, N + 1):
#     if A <= calc_sum(i) <= B:
#         total += i
total = sum(i for i in range(1, N + 1) if A <= calc_sum(i) <= B)

print(total)
