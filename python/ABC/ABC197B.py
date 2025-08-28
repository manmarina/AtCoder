H, W, X, Y = map(int, input().split())
S = [input().strip() for _ in range(H)]

x, y = X - 1, Y - 1  # 0-indexed

ans = 1  # 自分のマス

# 上
i = x - 1
while i >= 0 and S[i][y] == '.':
    ans += 1
    i -= 1

# 下
i = x + 1
while i < H and S[i][y] == '.':
    ans += 1
    i += 1

# 左
j = y - 1
while j >= 0 and S[x][j] == '.':
    ans += 1
    j -= 1

# 右
j = y + 1
while j < W and S[x][j] == '.':
    ans += 1
    j += 1

print(ans)
