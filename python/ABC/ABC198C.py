from math import ceil, sqrt

R, X, Y = map(int, input().split())

d2 = X * X + Y * Y  # 距離の二乗

if d2 < R * R:
    # 距離が R 未満なので 1 回では届かないが、2 回あれば必ず届く
    print(2)
else:
    # d = sqrt(d2) は実数（浮動小数）
    d = sqrt(d2)
    print(ceil(d / R))

"""
場合分け系
公式 + チャッピー
「距離が R より小さいときは 1 歩では絶対に届かないので 2 歩」というケースを見逃さない。

https://atcoder.jp/contests/abc198/tasks/abc198_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6917327c-c2f4-8324-8e7b-6da7860b8d5c
"""
