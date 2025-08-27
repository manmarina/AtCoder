N = int(input())
W = list(map(int, input().split()))

cs = [W[0]]
for i in range(1, N):
    cs.append(cs[i - 1] + W[i])

# print(cs)

ans = []
for i in range(N - 1):
    ans.append(abs(cs[N - 1] - cs[i] * 2))

# print(ans)

print(min(ans))
