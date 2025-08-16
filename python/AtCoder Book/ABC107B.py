H, W = map(int, input().split())
a = []
for i in range(H):
    a.append(input())


def compress(row_count, col_count, grid):
    compressed = []
    for row in grid:
        if '#' in row:
            compressed.append(list(row))

    row_count = len(compressed)

    for j in range(col_count - 1, -1, -1):
        for i in range(row_count):
            if compressed[i][j] == '#':
                break
        else:
            for k in range(row_count):
                del compressed[k][j]

    compressed = [''.join(row) for row in compressed]

    return compressed


print(*compress(H, W, a), sep='\n')
