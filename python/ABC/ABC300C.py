import sys

H, W = map(int, sys.stdin.readline().split())
S = [sys.stdin.readline().strip() for _ in range(H)]

# 準備
N = min(H, W)
ans = [0] * (N + 1)
dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# 全探索
for i in range(H):
    for j in range(W):
        if S[i][j] != '#':
            continue
        t = 0
        while True:
            ok = True
            # 4方向探索
            for dx, dy in dirs:
                x = i + (t + 1) * dx
                y = j + (t + 1) * dy
                if not (0 <= x < H and 0 <= y < W) or S[x][y] != '#':
                    ok = False
                    break  # グリッド外か#でないときは二重ブレイク
            if not ok:
                break
            t += 1  # 4方向すべて#ならt++
        if t >= 1:  # 二重ブレイクしたときにもここに来る t>=1ならansをカウントアップ
            ans[t] += 1

print(*ans[1:])  # サイズ1..N

"""
カーソル系（グリッド走査）
グリッド上の「X字型（対角方向に伸びる十字）」の大きさを数える問題です。

何を数える？
    各マスを中心に、4 つの対角方向（↖↗↙↘）のすべてに同じ長さだけ
    # が連続して伸びているとき、その中心にはサイズ s のクロスがあるとみなします。
    サイズは「中心からの“対角方向の歩数”」で、最小は 1（隣の対角マスが全部 #）。
    各中心について最大サイズを 1 回だけ数え上げます（小さいサイズに分配しない）。
"""
