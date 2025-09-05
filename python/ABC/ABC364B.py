H, W = map(int, input().split())
S = tuple(map(int, input().split()))
C = [input() for _ in range(H)]
X = input()

dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

r, c = S
r -= 1  # 0-indexに変換
c -= 1
for ch in X:
    dr, dc = dirs[ch]
    nr = r + dr
    nc = c + dc
    if 0 <= nr < H and 0 <= nc < W and C[nr][nc] == '.':
        r, c = nr, nc
print(r + 1, c + 1)  # 1-indexで出力
