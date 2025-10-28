from collections import defaultdict


N = int(input())
S = input()

if '-' not in S:  # 駆使がなければ終了
    print(-1)
    exit()

# ランレングス圧縮
i = 0
dd = defaultdict(int)
while i < N:
    j = i
    while j < N and S[i] == S[j]:
        j += 1
    dd[S[i]] = max(dd[S[i]], j - i)
    i = j

# print(dd)
print(dd['o'] if dd['o'] != 0 else -1)  # 串だけのときは-1

"""
ランレングス圧縮
329Cと同じ解法

https://atcoder.jp/contests/abc299/tasks/abc299_c
https://drken1215.hatenablog.com/entry/2023/04/29/163000
"""
