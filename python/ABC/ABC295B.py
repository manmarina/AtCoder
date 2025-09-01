R, C = map(int, input().split())
B = [list(input().strip()) for _ in range(R)]
# print(B)

bombs = []
# 爆弾の位置の配列を作成
for r in range(R):
    for c in range(C):
        if B[r][c].isdigit():
            bombs.append((r, c, int(B[r][c])))

# print(bombs)

# 爆弾のダイヤ範囲を '.' に
for i, j, p in bombs:
    for dx in range(-p, p + 1):
        x = i + dx
        if not (0 <= x < R):
            continue

        # rem は remaining（残り）の略　マンハッタン距離の条件 |dx| + |dy| ≤ p から「dy に許される最大値」
        rem = p - abs(dx)
        for dy in range(-rem, rem + 1):
            y = j + dy
            if 0 <= y < C:
                B[x][y] = '.'

# 出力
for row in B:
    print(*row, sep='')
