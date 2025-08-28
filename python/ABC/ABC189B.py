N, X = map(int, input().split())
VP = [list(map(int, input().split())) for _ in range(N)]

alc = 0
for i, (v, p) in enumerate(VP, 1):
    alc += v * p
    if alc > X * 100:
        print(i)
        break
else:
    print(-1)
