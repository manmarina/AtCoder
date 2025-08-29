from itertools import combinations

N, W = map(int, input().split())
A = list(map(int, input().split()))

ok = [False] * (W + 1)

# 1個の場合
for a in A:
    if a <= W:
        ok[a] = True

# 2個の場合
for a, b in combinations(A, 2):
    s = a + b
    if s <= W:
        ok[s] = True

# 3個の場合
for a, b, c in combinations(A, 3):
    s = a + b + c
    if s <= W:
        ok[s] = True

print(sum(ok))
