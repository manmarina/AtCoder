H, W = map(int, input().split())
S = [input() for i in range(H)]


def add_num(y, x):
    dirs = [(-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)]
    for dy, dx in dirs:
        ny = y + dy
        nx = x + dx
        if ny < 0 or ny >= H or nx < 0 or nx >= W:
            continue
        if answer[ny][nx] != '#':
            answer[ny][nx] += 1


# print(S)

answer = [[0 if char == '.' else '#' for char in s] for s in S]

# print(answer)

for i, s in enumerate(S):
    for j, char in enumerate(s):
        if char == '#':
            add_num(i, j)

for row in answer:
    print(*row, sep='')
