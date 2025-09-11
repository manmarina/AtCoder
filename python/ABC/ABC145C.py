from itertools import permutations
from math import hypot
from statistics import mean


N = int(input())
xy = [list(map(int, input().split()))for _ in range(N)]
# print(xy)

ans = []
for t in permutations(xy, N):
    temp = []
    for i in range(1, N):
        temp.append(hypot(t[i - 1][0] - t[i][0], t[i - 1][1] - t[i][1]))
    ans.append(sum(temp))

# print(ans)
print(mean(ans))
