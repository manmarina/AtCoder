import sys

input = sys.stdin.readline
N, Q = map(int, input().split())

# pc[v]: バージョン v の台数（v=1..N 初期は1台ずつ）
pc = [0] + [1] * N

O = 1  # 最古のバージョン
out = []

for _ in range(Q):
    X, Y = map(int, input().split())
    moved = 0
    # O を X まで進め、通過する全バージョンの台数を Y に集約
    while O <= X:
        moved += pc[O]
        pc[Y] += pc[O]
        # pc[O] を 0 にしなくても O は二度と参照しないが、明示的に消してもOK
        pc[O] = 0
        O += 1
    out.append(str(moved))

print("\n".join(out))

"""
単調ポインタ法（one-pass / 一本スキャン）
公式xチャッピー

単調ポインタ法（one-pass / 一本スキャン）
最「古」ポインタ O を 絶対に後退させずに 右へだけ進める手法です。
ループは各 v をちょうど一度だけ通過するので、見かけは二重ループでも 合計 O(N+Q) に収まります。

デバッグをしてようやく理解できた。

https://atcoder.jp/contests/abc426/tasks/abc426_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68e110e7-8e34-8323-b505-f12b436260da
"""
