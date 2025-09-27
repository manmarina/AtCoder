N = int(input())
A = list(map(int, input().split()))
# print(A)

B = [i for i in range(1, N + 1)]
ans = [0] * N
for i in range(N):
    if A[i] != -1:
        if A[i] not in B:
            print("No")
            exit()
        B.remove(A[i])
        ans[i] = A[i]
        # print(B)
        # print(ans)

for i in range(N):
    if ans[i] == 0:
        ans[i] = B.pop()
# print(B)
print("Yes")
print(*ans)
