N = int(input())
h = list(map(int, input().split()))

ans = h[0]
for i in range(N - 1):
    if h[i] < h[i + 1]:
        ans = h[i + 1]
    else:
        break
print(ans)
