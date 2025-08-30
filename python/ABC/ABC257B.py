N, K, Q = map(int, input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))


def to_pos(Q):
    count = 0
    for i, g in enumerate(grid):
        if g == 1:
            count += 1
        if count == Q:
            return i


grid = [0] * (N + 1)
for k in A:
    grid[k] = 1

# print(grid)

for Q in L:
    q = to_pos(Q)

    if q == N:
        continue
    if grid[q + 1] == 1:
        continue
    else:
        grid[q] = 0
        grid[q + 1] = 1

# print(grid)
print(*[i for i, g in enumerate(grid) if g == 1])
