H, W = map(int, input().split())
a = [input() for i in range(H)]
al = []
for str in a:
    al.append([*str])

# 行を削除
for i in range(H - 1, -1, -1):
    for char in al[i]:
        if char == '#':
            break
    else:
        al.pop(i)

# 列を削除
for j in range(W - 1, -1, -1):
    for row in al:
        if row[j] == '#':
            break
    else:
        for row in al:
            row.pop(j)

for row in al:
    print(*row, sep='')
