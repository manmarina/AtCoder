from itertools import permutations


N, K = map(int, input().split())
T = [list(map(int, input().split()))for _ in range(N)]
# print(T)

ans = []
for route in permutations(range(1, N)):
    route = list(route)
    route.append(0)
    route.insert(0, 0)
    # print(route)

    time = 0
    for a, b in zip(route, route[1:]):
        time += T[a][b]
    ans.append(time)

# print(ans)
print(ans.count(K))
