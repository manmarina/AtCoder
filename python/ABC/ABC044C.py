from itertools import combinations
from statistics import mean

N, A = map(int, input().split())
x = list(map(int, input().split()))

count = 0
for i in range(1, N + 1):
    for cmb in combinations(x, i):
        if mean(cmb) == A:
            count += 1

print(count)
