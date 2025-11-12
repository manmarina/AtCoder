from collections import defaultdict
from itertools import combinations


N = int(input())
S = [input() for _ in range(N)]

# okに該当する頭文字の個数をカウントする連想配列を作成
dd = defaultdict(int)  # 頭文字 -> その頭文字の文字列の数
ok = {'M', 'A', 'R', 'C', 'H'}
for s in S:
    if s[0] in ok:
        dd[s[0]] += 1
# print(dd)

# 頭文字3つの組み合わせを全探索
ans = 0
for a, b, c in combinations(dd.keys(), 3):
    ans += dd[a] * dd[b] * dd[c]  # 3つの頭文字の数の総積を加算
print(ans)

"""
組合せ全探索(combinations)
各頭文字の文字列の個数をカウントする。
頭文字の組み合わせを全探索して、各頭文字の数の総積の総和が答えとなる。

https://atcoder.jp/contests/abc089/tasks/abc089_c
"""
