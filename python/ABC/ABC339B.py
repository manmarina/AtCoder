H, W, N = map(int, input().split())

# 盤：False=白 '.' / True=黒 '#'
board = [[False] * W for _ in range(H)]

r, c = 0, 0          # スタートは (0,0)
dir = 0              # 0:上, 1:右, 2:下, 3:左
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for _ in range(N):
    if not board[r][c]:        # 白
        dir = (dir + 1) % 4    # 右を向く
        board[r][c] = True     # 黒に反転
    else:                      # 黒
        dir = (dir + 3) % 4    # 左を向く
        board[r][c] = False    # 白に反転

    r = (r + dr[dir] + H) % H  # Hを足すのは、負の数の%を-で返す他の言語でも対応できるようにするため
    c = (c + dc[dir] + W) % W  # pythonなら、HやWを足さなくても同じ動作になる

# 出力
for i in range(H):
    print(''.join('#' if board[i][j] else '.' for j in range(W)))
