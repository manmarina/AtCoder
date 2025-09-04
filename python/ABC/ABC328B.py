N = int(input())
D = list(map(int, input().split()))

count = 0
for m in range(1, N + 1):
    for d in range(1, D[m - 1] + 1):
        ms = set(str(m))
        ds = set(str(d))
        if len(ms) == 1 and ms == ds:
            count += 1
print(count)
