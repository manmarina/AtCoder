H, W = map(int, input().split())
S = [input() for _ in range(H)]
# print(S)

dirs = [(dx, dy) for dx in (-1, -0, 1)
        for dy in (-1, 0, 1) if not (dx == 0 and dy == 0)]
# print(dirs)

ok = ['s', 'n', 'u', 'k', 'e']

for i in range(H):
    for j in range(W):
        if S[i][j] == ok[0]:
            for dx, dy in dirs:
                x, y = i, j
                temp = [(x + 1, y + 1)]
                for s in range(1, len(ok)):
                    x = x + dx
                    y = y + dy
                    if not (0 <= x < H and 0 <= y < W):
                        break
                    if S[x][y] != ok[s]:
                        break
                    temp.append((x + 1, y + 1))
                else:
                    for row in temp:
                        print(*row)

"""
カーソル系
8方向に走査
配列の範囲外はスキップするタイプ
"""
