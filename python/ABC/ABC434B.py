N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]
# print(AB)

bird = [[] for _ in range(M + 1)]
# print(bird)

for A, B in AB:
    bird[A].append(B)
# print(bird)

for i in range(1, M + 1):
    print(sum(bird[i]) / len(bird[i]))
