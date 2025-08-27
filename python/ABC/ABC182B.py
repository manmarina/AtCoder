N = int(input())
A = list(map(int, input().split()))

best_cnt = 0
best_k = 2
for k in range(2, max(A) + 1):
    cnt = sum(a % k == 0 for a in A)
    if cnt >= best_cnt:
        best_cnt = cnt
        best_k = k
print(best_k)
