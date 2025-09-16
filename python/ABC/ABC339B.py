H, W, N = map(int, input().split())

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
grid = [['.'] * W for _ in range(H)]
# print(grid)

# 問題文の通りに色を変えながら向きを変えて進む
x, y = 0, 0
r = 0
for _ in range(N):
    if grid[x][y] == '.':
        grid[x][y] = '#'
        r += 1
    else:
        grid[x][y] = '.'
        r -= 1
    dx, dy = dirs[r % 4]
    x = (x + dx) % H
    y = (y + dy) % W

# 出力
for row in grid:
    print(*row, sep='')

"""
カーソル系
向きを表す配列dirを作成
左右90°回転をインデックスを進めることで表現
"""
