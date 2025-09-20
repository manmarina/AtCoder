N, M, K = map(int, input().split())
AB = [(tuple(map(int, input().split()))) for _ in range(K)]
# print(AB)

ans = [0] * (N + 1)
res = []
for a, b in AB:
    ans[a] += 1
    if ans[a] == M:
        res.append(a)
print(*res)
