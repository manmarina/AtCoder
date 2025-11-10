N, Q = map(int, input().split())
A = list(map(int, input().split()))
Query = [list(map(int, input().split())) for _ in range(Q)]

A2 = A + A  # Aを2回繰り返した配列を作成
# print(A2)

cs = [0]  # A2の累積和
for i in range(len(A2)):
    cs.append(cs[i] + A2[i])
# print(cs)

shift = 0  # インデックスをシフトする変数
for q in Query:
    if q[0] == 1:
        _, c = q
        shift = (shift + c) % N  # 回転を考慮してシフト値を変更する
    else:  # q[0] == 2:
        _, l, r = q
        print(cs[r + shift] - cs[l - 1 + shift])  # シフト値を加味して区間和を求める

"""
計算量を削減したシミュレーション + 二重配列の累積和
リトライ
回転は“配列を動かさずに”先頭位置のオフセットだけ持つ
累積和は “二重配列” に乗せる

https://atcoder.jp/contests/abc425/tasks/abc425_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68d7e92f-bc70-8333-90e3-a9d04186068d
"""
