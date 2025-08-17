N, K = map(int, input().split())

ans = 0
for a in range(1, N + 1):
    for b in range(1, N + 1):
        if (a + b) % K != 0:
            continue
        else:
            for c in range(1, N + 1):
                if (b + c) % K != 0 or (a + c) % K != 0:
                    continue
                else:
                    ans += 1

print(ans)
