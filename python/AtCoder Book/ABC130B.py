N, X = map(int, input().split())
L = list(map(int, input().split()))


def distance(times):
    for i in range(times):
        if i == 0:
            d = 0
        else:
            d += L[i - 1]
    return d


for i in range(1, N + 1 + 1):
    # print(distance(i))
    if X < distance(i):
        print(i - 1)
        break
else:
    print(N + 1)
