N = int(input())
A = list(map(int, input().split()))
# print(A)

ans = 0
for i in range(N):
    for j in range(i + 1, N + 1):
        sum_ = sum(A[i:j])
        # print(i, j, sum_)
        for k in A[i:j]:
            if sum_ % k == 0:
                break
        else:
            ans += 1
print(ans)
