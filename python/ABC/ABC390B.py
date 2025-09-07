N = int(input())
A = list(map(int, input().split()))
# print(A)

a0, a1 = A[0], A[1]
for i in range(1, N - 1):
    if A[i + 1] * a0 != A[i] * a1:  # クロス積が等しければ公比数列
        print("No")
        break
else:
    print("Yes")
