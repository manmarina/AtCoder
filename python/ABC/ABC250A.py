H, W = map(int, input().split())
R, C = map(int, input().split())

ans = 0
if R > 1:  # 上
    ans += 1
if C > 1:  # 左
    ans += 1
if R < H:  # 下
    ans += 1
if C < W:  # 右
    ans += 1
print(ans)
