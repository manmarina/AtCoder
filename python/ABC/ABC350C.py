N = int(input())
A = list(map(int, input().split()))

ans = []
flag = True
while flag:
    flag = False
    for i in range(N - 1):
        if A[i] > A[i + 1]:
            A[i], A[i + 1] = A[i + 1], A[i]
            ans.append((i + 1, i + 2))
            flag = True

print(len(ans))
for i in range(len(ans)):
    print(*ans[i])

"""
TLE

https://atcoder.jp/contests/abc350/tasks/abc350_c
"""
