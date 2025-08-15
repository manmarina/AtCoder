H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(input())


def map_mine(initial_map, rows, cols):
    answer_map = [[0 if v == '.' else '#' for v in row] for row in initial_map]
    DX = [1, 1, 1, 0, 0, -1, -1, -1]
    DY = [-1, 0, 1, -1, 1, -1, 0, 1]

    for i in range(rows):
        for j in range(cols):
            if initial_map[i][j] == '.':
                continue
            else:
                for di, dj in zip(DX, DY):
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= H or nj < 0 or nj >= W:
                        continue
                    if initial_map[ni][nj] != '#':
                        answer_map[ni][nj] += 1

    return answer_map


for row in map_mine(S, H, W):
    print(*row, sep='')
