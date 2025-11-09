from bisect import bisect_left


N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    idx = bisect_left(A, A[i] * 2)  # 2倍の大きさのもちのインデックス
    # print(i, idx, N - idx)
    ans += N - idx  # 2倍の大きさのもちの数
print(ans)

"""
計算量を削減したシミュレーション + 二分探索
自分の大きさの倍以上のもちの数を二分探索で高速に求める。
しゃくとり法でも解けるらしい。

https://atcoder.jp/contests/abc388/tasks/abc388_c
"""
