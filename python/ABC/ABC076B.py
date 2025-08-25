N = int(input())
K = int(input())

ans = 1
for i in range(N):
    if ans < K:
        ans += ans
    else:
        ans += K

print(ans)
