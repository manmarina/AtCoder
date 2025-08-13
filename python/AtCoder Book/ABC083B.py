N, A, B = map(int, input().split())

total = 0
for i in range(1, N + 1):
    sum_digit = 0
    num = i
    while num > 0:
        sum_digit += num % 10
        num //= 10
    if A <= sum_digit <= B:
        total += i

print(total)
