from itertools import combinations
from collections import defaultdict
N, M = map(int, input().split())
KX = [list(map(int, input().split()))for _ in range(M)]
# print(KX)

dd = defaultdict(set)
for kx in KX:
    k, *x = kx
    # print(k, x)

    for p in combinations(x, 2):
        # print(p)

        p1, p2 = p
        dd[p1].add(p2)
        dd[p2].add(p1)
# print(dd)

ok = {i for i in range(1, N + 1)}
# print(ok)

for i, s in dd.items():
    temp = {i, *s}
    # print(temp)

    if temp != ok:
        print("No")
        break
else:
    print("Yes")
