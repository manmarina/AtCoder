H, W, X, Y = map(int, input().split())
S = [input() for _ in range(H)]
T = input()

dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1), }
seen = set()  # 通過した'@'の座標

# 0-index へ
x, y = X - 1, Y - 1
for t in T:
    dx, dy = dirs[t]
    nx, ny = x + dx, y + dy

    # 境界＆壁チェック
    if 0 <= nx < H and 0 <= ny < W and S[nx][ny] != '#':
        x, y = nx, ny
        if S[x][y] == '@':
            seen.add((x, y))
            # print(seen)

print(x + 1, y + 1, len(seen))
