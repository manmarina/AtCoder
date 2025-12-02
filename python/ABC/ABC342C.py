from collections import defaultdict


N = int(input())
S = input()
Q = int(input())
Query = []
for _ in range(Q):
    c, d = input().split()
    Query.append((c, d))
# print(Query)

dd = defaultdict(list)
for i in range(N):
    dd[S[i]].append(i)
# print(dd)

for a, b in Query:
    nums = dd[a]
    dd[a] = []
    dd[b].extend(nums)  # extendがO(b)なので低速
# print(dd)

T = [0] * N
for k, v in dd.items():
    for idx in v:
        T[idx] = k
print(*T, sep='')

"""
TLE
"""
