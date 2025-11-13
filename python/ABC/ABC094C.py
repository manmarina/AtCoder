N = int(input())
X = list(map(int, input().split()))  # インデックス -> 値

Xs = sorted(X)
# print("Xs:", Xs)

Xsr = [0] * (N + 1)
for i in range(N):
    Xsr[Xs[i]] = i
# print("Xsr:", Xsr)

A = [0] * N
for i in range(N):
    A[i] = Xsr[X[i]]
# print("A:", A)

r = Xs[N // 2]
l = Xs[N // 2 - 1]
for a in A:
    if a < N // 2:
        print(r)
    else:
        print(l)

"""
RE
"""
