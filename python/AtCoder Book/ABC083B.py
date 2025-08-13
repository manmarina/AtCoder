N, A, B = map(int, input().split())


def calc_sum(num):
    sum_digit = 0
    while num > 0:
        sum_digit += num % 10
        num //= 10
    return sum_digit


total = 0
for i in range(1, N + 1):
    if A <= calc_sum(i) <= B:
        total += i

print(total)
