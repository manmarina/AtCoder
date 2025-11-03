N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
# print(A)

even = []
for i in range(N):
    if A[i] % 2 == 0:
        even.append(A[i])
        if len(even) == 2:
            break
odd = []
for i in range(N):
    if A[i] % 2 == 1:
        odd.append(A[i])
        if len(odd) == 2:
            break


if len(even) <= 1:
    even = []

if len(odd) <= 1:
    odd = []

# print(even)
# print(odd)

print(max(sum(even), sum(odd)))

"""
数学的な気づき系 WA
偶奇を考える

偶数の和は：
偶数 + 偶数
奇数 + 奇数
で作れます。
したがって、
偶数の中で大きい2つ
奇数の中で大きい2つ
をそれぞれ求めて、それらの和のうち最大を答えればOKです。

https://atcoder.jp/contests/abc272/tasks/abc272_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69084f3c-9eb0-8321-aa28-f9d84893c5e5
"""
