N = int(input())
S = input()

dir = 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
x = 0
y = 0

for s in S:
    if s == 'S':
        x += dx[dir]
        y += dy[dir]
    else:  # s == 'R'
        dir = (dir + 1) % 4

print(x, y)
