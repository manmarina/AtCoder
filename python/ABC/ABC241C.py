import sys

input = sys.stdin.readline
N = int(input())
S = [input().strip() for _ in range(N)]

dirs = [(0, 1), (1, 0), (1, 1), (1, -1)]  # →, ↓, ↘, ↙

for i in range(N):
    for j in range(N):
        for di, dj in dirs:
            ei = i + di * 5
            ej = j + dj * 5
            # 6マス先まで届くか（始点含めて長さ6）
            if not (0 <= ei < N and 0 <= ej < N):
                continue
            cnt = 0
            for k in range(6):
                ni = i + di * k
                nj = j + dj * k
                if S[ni][nj] == '#':
                    cnt += 1
            if cnt >= 4:
                print("Yes")
                exit()
print("No")

"""
全探索
チャッピー
「盤面上の長さ6の直線（横・縦・斜め）に ‘#’ が4個以上ある場所が1つでもあるか？」を判定します。
最初に6マス先まで届くかを判定してから数える（もしくは盤外に出たら break して不採用）。
でないと実質「長さ6未満」の部分列でも count>=4 になれば誤って Yes になります。

https://atcoder.jp/contests/abc241/tasks/abc241_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68dceb03-655c-8325-81d9-a6055e6e3621
"""
