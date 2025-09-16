N = int(input())
A = [input() for _ in range(N)]
# print(A)

dirs = [(dx, dy) for dx in (-1, 0, 1)
        for dy in (-1, 0, 1) if not (dx == 0 and dy == 0)]
# print(dirs)

ans = []
for i in range(N):
    for j in range(N):
        for dx, dy in dirs:
            x, y = i, j
            temp = []
            for _ in range(N):
                temp.append(A[x][y])
                x = (x + dx) % N
                y = (y + dy) % N
            ans.append(''.join(temp))

# print(ans)
print(*max(ans), sep='')
