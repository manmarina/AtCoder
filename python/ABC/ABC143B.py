from itertools import combinations

N = int(input())
d = list(map(int, input().split()))

ans = 0
for x, y in combinations(d, 2):
    ans += x * y
print(ans)
