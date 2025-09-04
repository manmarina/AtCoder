N, S, M, L = map(int, input().split())

ans = 10**18
for s in range(18):  # 全部6コパックで買っても100個買うには17パックあれば良い
    for m in range(18):
        rem = N - s * 6 - m * 8
        if rem <= 0:
            l = 0
        else:
            l = -(-rem // 12)
        total = S * s + M * m + L * l
        ans = min(ans, total)
print(ans)
