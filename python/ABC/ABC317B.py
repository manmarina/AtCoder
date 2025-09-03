N = int(input())
A = list(map(int, input().split()))

A.sort()
# print(A)
for i in range(1, N):
    if A[i] - A[i - 1] != 1:
        print(A[i] - 1)
        break
