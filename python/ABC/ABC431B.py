X = int(input())
N = int(input())
W = [0] + list(map(int, input().split()))
# print(W)

Q = int(input())
P = [int(input()) for _ in range(Q)]
# print(P)

parts = [False] * (N + 1)
# print(parts)

for p in P:
    if not parts[p]:
        parts[p] = True
        X += W[p]
        print(X)
    else:
        parts[p] = False
        X -= W[p]
        print(X)

"""
AC
"""
