from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

INF = 2 * 10**5
ans = INF
dd = defaultdict(lambda: -1)  # 初期値を-1に　Ai -> インデックス
for i in range(N):
    if dd[A[i]] != -1:  # ddにインデックスが格納されている時
        ln = i - dd[A[i]] + 1  # 区間長を求める
        ans = min(ans, ln)  # 区間長が最短なら更新する
        dd[A[i]] = i  # Aiのインデックスを更新する
    else:
        dd[A[i]] = i  # Aiのインデックスを更新する

print(ans if ans != INF else -1)  # ansが更新されなければ-1

"""
連想配列
Ai -> インデックス を格納する連想配列を作成して区間長を求める。

https://atcoder.jp/contests/abc395/tasks/abc395_c
"""
