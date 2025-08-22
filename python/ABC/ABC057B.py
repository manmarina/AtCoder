N, M = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(N)]
cd = [list(map(int, input().split())) for i in range(M)]

# print(ab)
# print(cd)

temp = []
dl = []
for i in range(N):
    for j in range(M):
        dis = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
        temp.append(dis)
    dl.append(temp.copy())
    temp.clear()

# print(dl)
for i in dl:
    print(i.index(min(i)) + 1)
