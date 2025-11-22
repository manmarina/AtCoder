from bisect import bisect_left, bisect_right

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
print(A)
print(B)

# X の範囲を広めに取る（0 ～ 10^9+1 くらい）
lo, hi = 0, 10**9 + 1  # [lo, hi] の最小の X を探すイメージで、ここでは hi は十分大きい

while lo < hi:
    mid = (lo + hi) // 2

    # mid 以下の A の個数（= seller）
    seller = bisect_right(A, mid)
    # mid 以上の B の個数（= buyer）
    buyer = M - bisect_left(B, mid)

    if seller >= buyer:
        # 条件を満たした → もっと小さい X がないか左側を探す
        hi = mid
    else:
        # まだ足りない → もっと右側（大きい X）を探す
        lo = mid + 1

print(lo)

"""
解で二分探索
seller(X) ≥ buyer(X) を満たす最小の Xを探す。
「最小」を探すので左寄せ版。
チャッピー

https://atcoder.jp/contests/abc312/tasks/abc312_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69214aed-f2e0-8324-8082-4e6977ccf1fb
"""
