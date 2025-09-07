N = int(input())
A = list(map(int, input().split()))
# print(A)

r = A[1] / A[0]
for i in range(1, N - 1):
    if A[i + 1] / A[i] != r:
        print("No")
        break
else:
    print("Yes")
