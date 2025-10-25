from collections import defaultdict


N = int(input())
A = list(map(int, input().split()))

cnt = defaultdict(int)
ans = []
for i, a in enumerate(A, 1):  # 左から走査
    cnt[a] += 1
    if cnt[a] == 2:  # 同じ数字は3個ある　その2個目がでたら
        ans.append((i, a))  # （そのインデックス=f(i)、その数字）を格納
ans.sort()  # インデックスでソート

# print(ans)
print(*[a for _, a in ans])  # 数字を出力

"""
問題文の理解が難解系

何を出力すればよいのかがわかりにくい。
出力例1を読んでわかった。

https://atcoder.jp/contests/abc306/tasks/abc306_c
"""
