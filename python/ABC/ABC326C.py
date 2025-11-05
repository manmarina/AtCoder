import bisect

N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

res = 0
for i in range(N):  # 左端を決める
    x = A[i]  # 左端の座標
    # x + M以上となるインデックス -> x + Mより小さいインデックスはbisect_left()-1
    it = bisect.bisect_left(A, x + M)  # 右端の座標（it-1）

    res = max(res, it - i)  # it - 1 - (i - 1) 区間に入る要素の個数

print(res)

"""
二分探索
二分探索（bisect_left()）の教育的問題

けんちょん
https://drken1215.hatenablog.com/entry/2023/11/11/204912

https://atcoder.jp/contests/abc326/tasks/abc326_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/project
"""
