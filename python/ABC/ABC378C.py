from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

ans = []
dd = defaultdict(int)  # Ai ->　出現位置
for i in range(N):
    if dd[A[i]] == 0:  # 出現したことがない時
        ans.append(-1)  # -1を格納
    else:  # 出現したことがあるときは
        ans.append(dd[A[i]])  # 出現位置を格納
    dd[A[i]] = i + 1
print(*ans)

"""
連想配列
1≤Ai≤10^9という制約を考えると、単純な配列だと 10^9ものサイズが必要になってしまう。
このようなとき、連想配列が活躍する。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2024/11/03/165455

https://atcoder.jp/contests/abc378/tasks/abc378_c
"""
