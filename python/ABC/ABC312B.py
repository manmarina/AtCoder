N, M = map(int, input().split())
S = [input().strip() for _ in range(N)]

ans = []

# 相対座標セットを用意
blk_tl = [(r, c) for r in range(3) for c in range(3)]              # 左上3x3(黒)
ring_tl = [(r, c) for r in range(4)
           for c in range(4) if not (r < 3 and c < 3)]  # 左上外周(白)

blk_br = [(r, c) for r in range(6, 9) for c in range(6, 9)]        # 右下3x3(黒)
ring_br = [
    (r,
     c) for r in range(
        5,
        9) for c in range(
            5,
            9) if not (
                6 <= r <= 8 and 6 <= c <= 8)]  # 右下外周(白)

for i in range(N - 9 + 1):
    for j in range(M - 9 + 1):
        ok = (
            all(S[i + r][j + c] == '#' for r, c in blk_tl) and
            all(S[i + r][j + c] == '.' for r, c in ring_tl) and
            all(S[i + r][j + c] == '#' for r, c in blk_br) and
            all(S[i + r][j + c] == '.' for r, c in ring_br)
        )
        if ok:
            ans.append((i + 1, j + 1))

for i, j in ans:
    print(i, j)
