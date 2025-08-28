A, B, C, D = map(int, input().split())

den = C * D - B
if den <= 0:
    print(-1)
else:
    # 0 回で既に満たす場合にも対応（A=0なら0が出る）
    print((A + den - 1) // den)  # A // den の切り上げ除算
