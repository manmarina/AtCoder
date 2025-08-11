N, M = map(int, input().split())

city = [[] for i in range(N)]
for i in range(M):
    A, B = map(int, input().split())
    city[A - 1].append(B)
    city[B - 1].append(A)

for i in range(N):
    city[i].sort()
    print(len(city[i]), *city[i])
