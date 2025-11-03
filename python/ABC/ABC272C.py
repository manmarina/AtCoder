N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)
# print(A)

mx = A[0]
for i in range(1, N):
    if (mx + A[i]) % 2 == 0:
        print(mx + A[i])
        exit()
else:
    print(-1)

"""
WA

https://atcoder.jp/contests/abc272/tasks/abc272_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69084f3c-9eb0-8321-aa28-f9d84893c5e5
"""
