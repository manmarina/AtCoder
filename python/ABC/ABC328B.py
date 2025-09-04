N = int(input())
D = list(map(int, input().split()))

count = 0
for m in range(1, N + 1):
    for d in range(1, D[m - 1] + 1):
        judge = set()
        m1, m2 = m, m
        d1, d2 = d, d
        if m >= 10:
            m1 = m // 10
            m2 = m % 10
        if d >= 10:
            d1 = d // 10
            d2 = d % 10
        judge.update([m1, m2, d1, d2])
        if len(judge) == 1:
            count += 1
print(count)
