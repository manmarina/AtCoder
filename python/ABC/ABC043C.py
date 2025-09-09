N = int(input().strip())
A = list(map(int, input().split()))

lo, hi = min(A), max(A)
ans = float('inf')
for t in range(lo, hi + 1):
    s = 0
    for a in A:
        d = a - t
        s += d * d
    ans = min(ans, s)
print(ans)
