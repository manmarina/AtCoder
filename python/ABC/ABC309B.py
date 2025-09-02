N = int(input())
A = [list(map(int, input().strip())) for _ in range(N)]

# Aをコピー
B = [row[:] for row in A]

# print(A)
# print(B)

# Pに外周の座標を作成（原点から時計回り）
P = []
# 上辺
for j in range(N):
    P.append((0, j))
# print(P)

# 右辺
for i in range(1, N):
    P.append((i, N - 1))
# print(P)

# 下辺
for j in range(N - 2, -1, -1):
    P.append((N - 1, j))
# print(P)

# 左辺
for i in range(N - 2, 0, -1):
    P.append((i, 0))
# print(P)

# 時計回りに1つ回す: 新しい場所に「直前の座標の値」を入れる
for idx, (i, j) in enumerate(P):
    pi, pj = P[(idx - 1 % len(P))]  # 0の1つ前は最後
    B[i][j] = A[pi][pj]

for row in B:
    print(*row, sep='')
