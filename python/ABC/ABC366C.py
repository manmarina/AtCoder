from collections import defaultdict


Q = int(input())
type = 0
bag = defaultdict(int)  # key=ボールの種類、value=ボールの数
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:  # ボールを袋に入れるとき
        if bag[q[1]] == 0:  # ボールの数がゼロなら
            type += 1  # ボールの種類を1つ増やす
        bag[q[1]] += 1
    elif q[0] == 2:  # ボールを袋から出すとき
        bag[q[1]] -= 1
        if bag[q[1]] == 0:  # ボールの数がゼロなら
            type -= 1  # ボールの種類を1つ減らす
    else:  # q[0] == 3:
        print(type)  # O(1)に変更
# print(bag)

"""
計算量を削減したクエリ処理
ボールの種類をO(1)で答えられる変数を用意する。

print(sum(1 for v in bag.values() if v != 0)) # O(N)
-> print(type) # O(1)に変更

https://atcoder.jp/contests/abc366/tasks/abc366_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68fb0e4c-84fc-8322-8383-e537817ca984
"""
