N = int(input())
A = [0] + list(map(int, input().split()))  # 1-indexed
# print(A)

# 変更前のルートの移動距離を求めておく
sum_ = 0
for i in range(1, N + 1):
    sum_ += abs(A[i] - A[i - 1])
sum_ += abs(A[-1])  # 最後に0に戻る移動距離を加える
# print("sum_:", sum_)

for i in range(1, N + 1):  # すべてのiについて
    pre = A[i - 1]
    cur = A[i]
    if i == N:  # 一番最後の観光スポットの時
        nex = 0  # 次は座標0に戻る
    else:
        nex = A[i + 1]
    before = abs(pre - cur) + abs(cur - nex)  # iを通るルート
    after = abs(pre - nex)  # iを通らないルート

    print(sum_ - before + after)  # iを通るルート分減らし、iを通らないルート分足す

"""
計算量を削減したシミュレーション
iごとに全体を再計算しなくて良いように考える。
変更前のルートの移動距離を計算しておき、iごとに差分のみ計算して求める。

https://atcoder.jp/contests/abc092/tasks/arc093_a
"""
