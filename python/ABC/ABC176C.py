N = int(input())
A = list(map(int, input().split()))

step = 0
for i in range(1, N):
    if A[i] - A[i-1] < 0:
        step += A[i-1] - A[i]
        A[i] = A[i-1]

# print(A)
print(step)

"""
基本実装問題

https://atcoder.jp/contests/abc176/tasks/abc176_c
"""
