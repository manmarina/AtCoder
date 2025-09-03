N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
# print(AB)

rank = {i: set() for i in range(1, N + 1)}
# print(rank)

for a, b in AB:
    rank[b].add(a)
# print(rank)

ans = [k for k, v in rank.items() if len(v) == 0]
print(ans[0] if len(ans) == 1 else -1)
