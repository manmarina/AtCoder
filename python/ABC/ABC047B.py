W, H, N = map(int, input().split())

pl = [[1 for i in range(W)] for j in range(H)]
xya = []
for i in range(N):
    x, y, a = map(int, input().split())
    xya.append((x, y, a))
# print(pl)
# print(xya)

for i in xya:
    if i[2] == 1:
        for j in pl:
            for k in range(i[0]):
                j[k] = 0
    elif i[2] == 2:
        for j in pl:
            for k in range(W - 1, i[0] - 1, -1):
                j[k] = 0
    elif i[2] == 3:
        for j in range(H - 1, H - i[1] - 1, -1):
            for k in range(W):
                pl[j][k] = 0
    elif i[2] == 4:
        for j in range(H - i[1]):
            for k in range(W):
                pl[j][k] = 0

# print(pl)
print(sum(map(sum, pl)))
