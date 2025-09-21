import sys

input = sys.stdin.readline
N = int(input())
S = input().strip()

posA = [i for i, ch in enumerate(S) if ch == 'A']  # 長さN
# print(posA)

# Aを偶数番(0,2,4,...)に置く場合
cost_even = 0
for k, i in enumerate(posA):
    cost_even += abs(i - 2 * k)

# Aを奇数番(1,3,5,...)に置く場合
cost_odd = 0
for k, i in enumerate(posA):
    cost_odd += abs(i - (2 * k + 1))

print(min(cost_even, cost_odd))

"""
発想の転換系
チャッピー
公式解説動画を見て理解

N 個の A と N 個の B からなり同じ文字が隣り合う箇所がない文字列は ABABAB..., BABABA... の 2 種類しかありません。
よって「 S を T にするには何回の操作が必要か？」というタイプの問題を 2 回解けば元の問題に答えることができます。

同じ文字が隣り合っている箇所に対して操作をする意味はありません。よって、操作の前後で A の順序が入れ替わることはありません。つまり、
ここがポイント！！
S の前から k 番目にある A は、T の前から k 番目にある Aの位置に移動します。
https://atcoder.jp/contests/abc421/editorial/13730
"""
