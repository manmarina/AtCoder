N, M = map(int, input().split())

line = set()  # 辺を管理するset
for _ in range(M):
    u, v = map(int, input().split())
    if u == v:  # 自己ループならスルー
        continue

    line.add((min(u, v), max(u, v)))  # setに辺（小さい頂点、大きい頂点）を追加

print(M - len(line))  # もとの辺の数から、実際に追加された辺の数を引いたものが削除する辺の数

"""
グラフ
399Cと似ているが、サイクルはそのままで良い。
自己ループと多重辺だけ削除する。

https://atcoder.jp/contests/abc393/tasks/abc393_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69082d76-8ee8-8320-a838-77a273b93c68
"""
