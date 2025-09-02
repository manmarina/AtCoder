H, W = map(int, input().split())
S = [input().strip() for _ in range(H)]

word = "snuke"
dirs = [(-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)]

# スタート位置を決める
for i in range(H):
    for j in range(W):
        if S[i][j] != word[0]:
            continue
        # スタート位置から8方向を選択
        for dx, dy in dirs:
            pos = []
            # 1方向内で1文字ずつチェック
            for k, ch in enumerate(word):
                nx = i + dx * k
                ny = j + dy * k
                # 配列の範囲外はスキップ
                if not (0 <= nx < H and 0 <= ny < W):
                    break
                # 文字が一致しなければスキップ
                if S[nx][ny] != ch:
                    break
                # 文字が一致したら座標を格納
                pos.append((nx + 1, ny + 1))  # 1-indexed
            else:
                # 全文字が一致したら座標を表示して終了
                for r, c in pos:
                    print(r, c)
                exit()
