N, M = map(int, input().split())

S = []
point = []
for i in range(N):
    S.append(input())
    point.append(0)

# print(S)
# print(point)

# 点数表を作成
for i in range(N):
    for j in range(M):
        if S[i][j] == 'o':
            point[i] += 2**j  # 各人の点数をビットフラグで格納

# print(point)


count = 0
for i in range(N):
    for j in range(i + 1, N):
        if point[i] | point[j] == 2**M - 1:  # ペアの点数のorが11111ならcount++
            count += 1

# print(point)

print(count)
