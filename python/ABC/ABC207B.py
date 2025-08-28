A, B, C, D = map(int, input().split())

den = C * D - B
if den <= 0:  # 到達可能性の判断
    print(-1)
else:
    x = 0
    # 条件: A + Bx <= C*D*x になる最小の x を探す
    while A + B * x > C * D * x:
        x += 1
    print(x)
