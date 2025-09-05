N = int(input())
A = [list(map(int, input().split()))for _ in range(N)]
# print(A)

pre = 1
for i in range(1, N + 1):
    mx = max(pre, i) - 1
    mn = min(pre, i) - 1
    ele = A[mx][mn]
    pre = ele

    # print(ele)
print(ele)
