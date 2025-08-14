N, M = map(int, input().split())
IPY = []
for i in range(1, M + 1):
    p, y = map(int, input().split())
    IPY.append([i, p, y])

IPY.sort(key=lambda x: (x[1], x[2]))
# print(IPY)

prefecture = 1
count = 1
for ipy in IPY:
    if ipy[1] != prefecture:
        prefecture = ipy[1]
        count = 1
        id = str(prefecture).zfill(6) + str(count).zfill(6)
        ipy.append(id)
        count += 1
    else:
        id = str(prefecture).zfill(6) + str(count).zfill(6)
        ipy.append(id)
        count += 1

IPY.sort(key=lambda x: x[0])
# print(IPY)

ids = [item[3] for item in IPY]
print(*ids, sep='\n')
