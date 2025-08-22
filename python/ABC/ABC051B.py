K, S = map(int, input().split())

count = 0
for X in range(K + 1):
    for Y in range(K + 1):
        Z = S - X - Y
        if Z < 0 or Z > K:
            continue
        count += 1

print(count)
