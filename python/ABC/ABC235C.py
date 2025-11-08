from collections import defaultdict


N, Q = map(int, input().split())
A = list(map(int, input().split()))
Query = [list(map(int, input().split())) for _ in range(Q)]
# print(Query)

dd = defaultdict(list)  # ai -> [出現位置のリスト]
for i in range(N):
    dd[A[i]].append(i + 1)  # 1-indexed
# print(dd)

for x, k in Query:
    if len(dd[x]) < k:  # [出現位置のリスト]がkより短い時
        print(-1)
    else:
        print(dd[x][k - 1])  # [出現位置のリスト]のk番目を出力する

"""
計算量を削減したクエリ処理 + 連想配列
リトライ
「データ構造系（連想配列での出現位置管理）」問題

https://atcoder.jp/contests/abc235/tasks/abc235_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68d356c3-2370-832f-ae8c-266469b34f84
"""
