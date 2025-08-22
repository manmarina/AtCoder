N, M = map(int, input().split())
students = [tuple(map(int, input().split())) for _ in range(N)]
checks = [tuple(map(int, input().split())) for _ in range(M)]

for x, y in students:
    best_j = 1
    ax, ay = checks[0]
    best_d = abs(x - ax) + abs(y - ay)
    for j in range(1, M):
        ax, ay = checks[j]
        d = abs(x - ax) + abs(y - ay)
        if d < best_d:  # タイは更新しない（小さいjを保持）
            best_d = d
            best_j = j + 1  # 1-index
    print(best_j)
