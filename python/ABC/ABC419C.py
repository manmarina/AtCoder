N = int(input())
R = []
C = []
for _ in range(N):
    r, c = map(int, input().split())
    R.append(r)
    C.append(c)

diff_R = max(R) - min(R)  # 行方向の最大幅
diff_C = max(C) - min(C)  # 列方向の最大幅

diff = max(diff_R, diff_C)  # 行、列の最大幅の大きい方

print(-(-diff // 2))  # 最大幅を2で割った切り上げ

"""
問題を言い換える系

@wiki
https://w.atwiki.jp/sport_programming/pages/269.html
RとCの範囲が大きい方について、2ずつ減らす（最後に1残ったら1減らす）ことを繰り返して0にするまでに必要な最小回数を求めればよい。
計算としては、2で割った切り上げということになる。

https://atcoder.jp/contests/abc419/tasks/abc419_c
"""
