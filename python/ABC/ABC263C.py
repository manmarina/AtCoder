from itertools import combinations


N, M = map(int, input().split())

A = [i for i in range(1, M + 1)]
# print(A)

for c in combinations(A, N):
    print(*c)

"""
組合せ全探索(combinations)
リトライ

combinationsを使用。デフォルトで辞書順出力される。
実質 C(M, N) 通りを辞書順で出力する問題です。

https://atcoder.jp/contests/abc263/tasks/abc263_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68df305f-f7c0-8324-a5f7-9e43fd39ec3d
"""
