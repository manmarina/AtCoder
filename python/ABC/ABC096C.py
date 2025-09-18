H, W = map(int, input().split())
s = [input() for _ in range(H)]
# print(s)

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for i in range(H):
    for j in range(W):
        if s[i][j] == '#':
            for dx, dy in dirs:
                x = i + dx
                y = j + dy
                if not (0 <= x < H and 0 <= y < W):
                    continue
                if s[x][y] == '#':
                    break
            else:  # '#'を囲む4方向に'#'がなければ早期終了
                print("No")
                exit()
else:
    print("Yes")

"""
カーソル系
DFSを使わない自力解

上下左右に隣り合う'#'があればよいので、
全探索して孤立する'#'が見つかったら早期終了
"""
