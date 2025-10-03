import sys

input = sys.stdin.readline
N = int(input())
P = list(map(int, input().split()))  # P[i] = 席iに最初にある料理番号

cnt = [0] * N   # cnt[k] = 回転k回で満足する人数
for i, pi in enumerate(P):
    # この料理 pi が「人 pi-1, pi, pi+1 の前に来る」ための回転kを数える
    for dj in (-1, 0, 1):  # 正面と左右両隣
        k = (pi + dj - i) % N  # 正面と左右両隣のときの回転量
        cnt[k] += 1

print(max(cnt))
print(cnt)

"""
計算量を削減したシミュレーション
公式xチャッピー
循環（円環）×オフセット集計（mod）×頻度カウント

「回転ごとに“嬉しい人数”を数えるためのオフセット集計（差分カウント）問題」です。

各 k に対して N 人の人がそれぞれ喜ぶかどうかを調べると O(N^2) となり、実行時間制限に間に合いません。

料理を基準に考える
席 i にある料理 pi に注目しましょう。
回転 k 回後、この料理 pi は席 (i + k) mod N に来ます。
満足するためには、(i + k) mod N が pi−1, pi, pi+1 のどれかに一致すればよい。
つまり方程式にすると：

i + k ≡ pi + dj (mod N)

k を解く
上の式を k について解くと：

k ≡ (pi + dj - i) (mod N)

https://atcoder.jp/contests/abc268/tasks/abc268_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68df53a4-d150-8323-976d-2762162535fc
"""
