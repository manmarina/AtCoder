S = [input() for _ in range(8)]
# print(S)

row = [False] * 8
col = [False] * 8

for i, sr in enumerate(S):
    if '#' in sr:
        row[i] = True
    for j, sc in enumerate(sr):
        if sc == '#':
            col[j] = True

# print(row)
# print(col)
print(row.count(False) * col.count(False))
