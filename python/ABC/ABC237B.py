H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# 転置
AT = list(zip(*A))   # 各要素はタプルになる

for row in AT:
    print(*row)
