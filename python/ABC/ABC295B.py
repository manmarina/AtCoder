R, C = map(int, input().split())
B = [input() for _ in range(R)]
# print(B)

# 爆発後のマップを作成
bombed = []
for b in B:
    bombed.append([*b])
# print(bombed)

# マップ上の爆弾を全探索
for i in range(R):
    for j in range(C):
        if B[i][j].isdecimal():
            # 爆発
            pow = int(B[i][j])
            for dx in range(-pow, pow + 1):
                for dy in range(-(pow - abs(dx)), pow - abs(dx) + 1):
                    # print(dx, dy)
                    x = i + dx
                    y = j + dy
                    # 爆発の範囲がマップ内か判定
                    if 0 <= x < R and 0 <= y < C:
                        bombed[x][y] = '.'

# 爆発後のマップを表示
for row in bombed:
    print(*row, sep='')

"""
カーソル系
何をする問題？
・RxC のグリッド
・文字は .（空き）,#（壁）,1〜9（爆弾の威力）
・すべての爆弾が同時に爆発し，爆弾マスからマンハッタン距離 ≤ 威力 のマスが . になる（壁も爆弾も消える）。
・最終状態のグリッドを出力。

必要なテクニック
同時更新の扱い
    更新（消去）をしながら次の爆弾を探すと「爆弾そのものを消して見逃す」恐れがある。
    → 先に爆弾の位置と威力を全部収集してから、まとめて消去処理。

マンハッタン距離の走査（ダイヤ型の内側だけ回す）
    爆弾 (i,j), 威力 p に対し
    for dx in [-p..p]: rem = p - |dx|; for dy in [-rem..rem]
    これで |dx| + |dy| ≤ p を満たす範囲だけを効率よく走査できる。
    範囲外チェック（0 ≤ x < R, 0 ≤ y < C）を忘れずに。

破壊の上書きは単純に '.' に
    壁 # でも爆弾でも、到達範囲なら . にしてOK。
    （自分自身の爆弾マスも距離0なので . になる。）
"""
