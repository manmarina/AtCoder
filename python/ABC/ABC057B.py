N, M = map(int, input().split())
ab = [list(map(int, input().split())) for i in range(N)]
cd = [list(map(int, input().split())) for i in range(M)]

# print(ab)
# print(cd)


dl = []
for x1, y1 in ab:
    temp = []
    for x2, y2 in cd:
        dis = abs(x1 - x2) + abs(y1 - y2)
        temp.append(dis)
    dl.append(temp)

# print(dl)
for i in dl:
    print(i.index(min(i)) + 1)
