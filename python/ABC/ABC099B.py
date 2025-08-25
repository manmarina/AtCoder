a, b = map(int, input().split())

tower = [0, 1]
for i in range(2, 999 + 1):
    tower.append(tower[i - 1] + i)
# print(tower)
dif = [0]
for i in range(1, 999):
    dif.append(tower[i + 1] - tower[i])
# print(dif[0])
ind = dif.index(b - a)
# print(ind)
print(tower[ind] - a)
