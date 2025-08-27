from itertools import combinations

N = int(input())
L = list(map(int, input().split()))

# print(L)

count = 0
for a, b, c in combinations(L, 3):
    if len({a, b, c}) < 3:
        continue

    x, y, z = sorted([a, b, c])
    if x + y > z:
        count += 1
print(count)
