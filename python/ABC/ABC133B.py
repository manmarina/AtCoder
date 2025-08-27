from math import isqrt

N, D = map(int, input().split())
X = [list(map(int, input().split())) for i in range(N)]

# print(X)

ans = 0
for i in range(N):
    for j in range(i + 1, N):
        s = 0
        for k in range(D):
            s += (X[i][k] - X[j][k])**2
        r = isqrt(s)
        if r**2 == s:
            ans += 1
print(ans)
