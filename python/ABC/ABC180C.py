N = int(input())

res = []
i = 1
while i * i <= N:
    if N % i == 0:
        res.append(i)
        if i * i != N:  # 平方根でなければ
            res.append(N // i)
    i += 1

res.sort()
for v in res:
    print(v)

"""
約数列挙
けんちょん
完全に約数列挙！！！！！
setを使わないなら、appendする前に、重複チェックをする。

https://atcoder.jp/contests/abc180/tasks/abc180_c
https://drken1215.hatenablog.com/entry/2020/10/21/194700
"""
