N, Q = map(int, input().split())

a = []
for i in range(N):
    a.append(list(map(int, input().split())))

answer = []
for i in range(Q):
    s, t = map(int, input().split())
    answer.append(a[s - 1][t])

for i in range(Q):
    print(answer[i])
