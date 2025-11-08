from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

B = sorted(A)
# print(B)

dd = defaultdict(int)
for i in range(N - 1):
    if B[i] != B[i + 1]:
        dd[B[i]] = sum(B[i + 1:])
# print(dd)

out = []
for a in A:
    out.append(dd[a])
print(*out)
