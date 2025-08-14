N, K = map(int, input().split())
h = []
for i in range(N):
    h.append(int(input()))

h.sort(reverse=True)

min = 10**9
for i in range(N + 1 - K):
    if min > h[i] - h[i + K - 1]:
        min = h[i] - h[i + K - 1]

print(min)
