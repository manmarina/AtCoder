N = int(input().strip())
A = [input().strip() for _ in range(N)]

dirs = [(dx, dy) for dx in (-1, 0, 1)
        for dy in (-1, 0, 1) if not (dx == 0 and dy == 0)]

print(A)
print(dirs)

best = "0"  # すべて '0' でもOKなように初期化
for i in range(N):
    for j in range(N):
        for dx, dy in dirs:
            r, c = i, j
            s = []
            for _ in range(N):
                s.append(A[r][c])
                r = (r + dx) % N
                c = (c + dy) % N
            cur = "".join(s)
            if cur > best:
                best = cur

print(best)
