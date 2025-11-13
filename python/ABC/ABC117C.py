N, M = map(int, input().split())
X = list(map(int, input().split()))

# 座標をソート
X.sort()

# 隣り合う差分を求める
diffs = []
for i in range(1, M):
    diffs.append(X[i] - X[i - 1])

# 差分を降順でソート
diffs.sort(reverse=True)
print(diffs)

# 全体の距離
res = X[-1] - X[0]

# 大きい差分から N-1 個だけ引く
# 座標の数より駒の数が大きいこともあるのでmin(len(diffs), N - 1)とする必要がある。
for i in range(min(len(diffs), N - 1)):
    res -= diffs[i]

print(res)

"""
貪欲法
けんちょん
https://drken1215.hatenablog.com/entry/2019/02/03/224100
N個のコマを置くということは、N個の区間で覆うということ。
つまりN-1個の覆われていない区間ができる。
N-1個の覆われていない区間を長い方から貪欲に選択して、全体の長さから引くと答えになる。

https://atcoder.jp/contests/abc117/tasks/abc117_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6915d025-eaf4-8321-a96f-278537c96ae5
"""
