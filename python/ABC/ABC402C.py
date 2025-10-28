from collections import defaultdict


N, M = map(int, input().split())
A = []
for _ in range(M):
    temp = list(map(int, input().split()))
    temp.pop(0)
    A.append(temp)
B = list(map(int, input().split()))
# print(A)
# print(B)

for i in range(M):
    for j in range(len(A[i])):
        # B.index(x) はリスト線形探索なので O(N) かかります。
        A[i][j] = B.index(A[i][j]) + 1  # ←ここがやばい
# print(A)

dd = defaultdict(int)
for a in A:
    dd[max(a)] += 1
# print(dd)

ans = 0
for i in range(1, N + 1):
    ans += dd[i]
    print(ans)

"""
計算量を削減したシミュレーション
TLE
六月
https://x.com/june19312/status/1914148087905587212"
食材の名前を克服する日付に変更する。
使われている食材で、最大の日付が克服する日。

https://atcoder.jp/contests/abc402/tasks/abc402_c
"""
