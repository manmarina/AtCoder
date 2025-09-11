from itertools import permutations


N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

ans = []
for per in permutations(range(1, N + 1)):
    ans.append(per)
ans.sort()

# print(ans)

idxp = ans.index(P)
idxq = ans.index(Q)
print(abs(idxp - idxq))
