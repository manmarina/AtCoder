from bisect import bisect_left


N, A, B = map(int, input().split())
S = input()

# aとbの累積和配列を作成
# appendするよりも速い
Xa = [0] * (N + 1)
Xb = [0] * (N + 1)
for i, ch in enumerate(S, 1):
    Xa[i] = Xa[i - 1] + (ch == 'a')
    Xb[i] = Xb[i - 1] + (ch == 'b')
print("Xa", Xa)
print("Xb", Xb)

# 二分探索
ans = 0
for i in range(N):  # 開始の接頭辞位置 終了はN-1まで!!
    na = A + Xa[i]  # "a" が A 個以上になるための閾値
    nb = B + Xb[i]  # "b" が B 個になる最初の位置の閾値
    print("na:", na, "nb:", nb)

    Ra = bisect_left(Xa, na)
    Rb = bisect_left(Xb, nb)
    # print("Ra:", Ra, "Rb:", Rb)

    Ra = max(Ra, i + 1)  # 空区間(j=i)は禁止 ### これがないとWA ###

    if Ra <= Rb - 1:  # Raのほうが、Rb-1よりも小さい時（チャッピー解説を参照）
        ans += (Rb - Ra)  # Rb - 1 - (Ra - 1) がiの時のA,Bを満たす組の個数

print(ans)


"""
累積和 + 二分探索
累積和配列を二分探索することで、O(N^2) -> O(N logN)に高速化。

解説
https://atcoder.jp/contests/abc430/editorial/14299
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69069477-39b8-8322-84d8-25a65021538d

https://atcoder.jp/contests/abc430/tasks/abc430_c
"""
