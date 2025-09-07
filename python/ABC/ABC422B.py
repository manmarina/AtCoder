H, W = map(int, input().split())
S = [input() for _ in range(H)]
# print(S)

dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
for i in range(H):
    for j in range(W):
        if S[i][j] != '#':
            continue
        count = 0
        for k in range(4):
            x, y = i, j
            dx, dy = dirs[k]
            nx, ny = x + dx, y + dy
            if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == '#':
                count += 1
        if count not in (2, 4):
            print("No")
            exit()
print("Yes")
