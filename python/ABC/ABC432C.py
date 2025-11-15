N, X, Y = map(int, input().split())
A = list(map(int, input().split()))

if min(A) * Y < max(A) * X:
    print(-1)
    exit()

A.sort()
# print(A)

total = A[0] * Y
diff = Y - X
ans = A[0]
# print(total)
for i in range(1, N):
    total_cur = A[i] * Y
    diff_cur = total_cur - total
    if diff_cur % diff != 0:
        print(-1)
        exit()
    else:
        ans += A[i] - diff_cur // diff
print(ans)
