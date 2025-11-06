N, K = map(int, input().split())

l = N % K
# r = abs((N // K + 1) * K - N)
r = K - N % K
print(min(l, r))

"""
シミュレーション系
結局のところ最終的には、
    NをKで割ったあまり (N % K)
    それをKから引いた値 (K - N % K)
を繰り返すことになる。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2020/04/05/155200

https://atcoder.jp/contests/abc161/tasks/abc161_c
"""
