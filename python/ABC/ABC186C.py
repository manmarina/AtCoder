def ok(v, b):
    while v:
        if v % b == 7:
            return False
        v //= b
    return True


N = int(input())
res = 0

for n in range(1, N + 1):
    if ok(n, 10) and ok(n, 8):
        res += 1

print(res)

"""
数学的な気づき系
8進数に変換する。
7が含まれる数をsetに追加してゆく。
自力解をさらにエレガントに！！

けんちょん
https://drken1215.hatenablog.com/entry/2020/12/19/224100

https://atcoder.jp/contests/abc186/tasks/abc186_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69104278-ae84-8321-b4c6-b1ae94a9715e
"""
