N = int(input())
A = list(map(int, input().split()))
# print(A)

ans = [A[0]]
for i in range(N - 1):
    a, b = A[i], A[i + 1]
    step = 1 if a < b else -1
    for x in range(a + step, b + step, step):
        ans.append(x)
print(*ans)
