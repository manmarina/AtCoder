N = int(input().strip())
XY = [tuple(map(int, input().split())) for _ in range(N)]

for i in range(N):
    xi, yi = XY[i]
    best_j = -1
    best_d2 = -1  # 二乗距離の最大値
    for j in range(N):
        if i == j:
            continue
        xj, yj = XY[j]
        dx = xi - xj
        dy = yi - yj
        d2 = dx * dx + dy * dy
        # ">": 同距離なら既存(best_j)が小さい方で残る
        if d2 > best_d2:
            best_d2 = d2
            best_j = j
    print(best_j + 1)  # 1-index
