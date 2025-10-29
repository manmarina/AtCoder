N = int(input())
N -= 1  # 0から始まり、N 番目の整数はN-1。
a = []

# 5進数に変換
while N:
    a.append(N % 5)
    N //= 5

if not a:
    a.append(0)

a.reverse()
# print(a)

# 0,2,4,6,8 に置き換え直す
for x in a:
    print(x * 2, end='')
print()

"""
数学的な気づき系
5進数に変換する。
解説
https://atcoder.jp/contests/abc336/editorial/9058
0から始まり、N 番目の整数はN-1。
つまり、N-1 を 5 進数に変換して、その後0,2,4,6,8 に置き換え直す。

https://atcoder.jp/contests/abc336/tasks/abc336_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69019c8a-c5f8-8321-9fce-3036dc5fec45
"""
