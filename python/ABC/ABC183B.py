Sx, Sy, Gx, Gy = map(int, input().split())

dx = Sy * (Gx - Sx) / (Gy + Sy)  # 辺の長さの比による比例計算
print(Sx + dx)
