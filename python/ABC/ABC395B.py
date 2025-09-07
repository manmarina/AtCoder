N = int(input())

for i in range(1, N + 1):
    row = []
    for j in range(1, N + 1):
        layer = min(i, j, N + 1 - i, N + 1 - j)  # 外周からのチェビシェフ距離
        row.append("#" if layer % 2 == 1 else '.')  # 距離の最小値が奇数なら'#'、偶数なら'.'
    print(*row, sep='')
