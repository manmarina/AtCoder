N, K = map(int, input().split())

cnt0 = N // K
ans = cnt0 ** 3

if K % 2 == 0:
    cntH = (N + K // 2) // K
    ans += cntH ** 3

print(ans)
