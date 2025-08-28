N = int(input())
APX = [list(map(int, input().split())) for _ in range(N)]

ans = 10**9
for a, p, x in APX:
    if a < x:
        if p < ans:
            ans = p
print(ans if ans < 10**9 else -1)
