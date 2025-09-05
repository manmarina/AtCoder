N, M = map(int, input().split())
A = list(map(int, input().split()))
X = [list(map(int, input().split())) for _ in range(N)]

sumv = [0] * M
for i in range(N):
    for j in range(M):
        sumv[j] += X[i][j]
# print(sumv)

ok = all(sumv[j] >= A[j] for j in range(M))
print("Yes" if ok else "No")
