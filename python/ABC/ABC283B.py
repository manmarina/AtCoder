N, M = map(int, input().split())

S = []
point = []
for i in range(N):
    S.append(input())
    point.append(0)

for i in range(N):
    for j in range(M):
        if S[i][j] == 'o':
            point[i] += 2**j

count = 0
for i in range(N):
    for j in range(i + 1, N):
        if point[i] | point[j] == 2**M - 1:
            count += 1

print(count)
