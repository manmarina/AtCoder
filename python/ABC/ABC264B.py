R, C = map(int, input().split())

grid = [[0] * 16 for i in range(16)]

for i in range(1, 16):
    grid[1][i] = 1
    grid[15][i] = 1
    grid[i][1] = 1
    grid[i][15] = 1

for i in range(3, 14):
    grid[3][i] = 1
    grid[13][i] = 1
    grid[i][3] = 1
    grid[i][13] = 1

for i in range(5, 12):
    grid[5][i] = 1
    grid[11][i] = 1
    grid[i][5] = 1
    grid[i][11] = 1

for i in range(7, 10):
    grid[7][i] = 1
    grid[9][i] = 1
    grid[i][7] = 1
    grid[i][9] = 1

if grid[R][C] == 1:
    print("black")
else:
    print("white")
