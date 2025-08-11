N, M = map(int, input().split())

AB = []
for i in range(M):
    AB.append(list(map(int, input().split())))

city = [[] for i in range(N)]
for i in range(M):
    city[AB[i][0] - 1].append(AB[i][1])
    city[AB[i][1] - 1].append(AB[i][0])

for i in range(N):
    city[i].sort()
    print(len(city[i]), *city[i])
