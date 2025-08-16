K, S = map(int, input().split())

ans = 0
for x in range(K + 1):
    y_min = max(0, S - x - K)
    y_max = min(K, S - x)
    if y_min <= y_max:
        ans += (y_max - y_min + 1)

print(ans)
