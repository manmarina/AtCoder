N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(M)]
# print(a)

friend = [[False] * N for _ in range(N)]
# print(friend)

for row in a:
    for i in range(len(row) - 1):
        l = row[i] - 1
        r = row[i + 1] - 1
        friend[l][r] = True
        friend[r][l] = True
# print(friend)

count = 0
for i in range(N):
    for j in range(i + 1, N):  # 隣接表の半分だけ走査
        if i != j:
            if not friend[i][j]:
                count += 1
print(count)

"""
無向グラフ
2次元配列（隣接表）を作成
隣接表の右上の領域のみカウントする
"""
