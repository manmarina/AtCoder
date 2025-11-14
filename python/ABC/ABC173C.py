H, W, K = map(int, input().split())
c = [input().strip() for _ in range(H)]

ans = 0

# 行の選び方：0 ～ (1<<H)-1
for mskH in range(1 << H):
    # 列の選び方：0 ～ (1<<W)-1
    for mskW in range(1 << W):
        # 盤面コピー（文字を書き換えたいので list にする）
        c2 = [list(row) for row in c]

        # mskH で 1 が立っている行を全部 'R' で塗りつぶす
        for y in range(H):
            if mskH & (1 << y):
                for x in range(W):
                    c2[y][x] = 'R'

        # mskW で 1 が立っている列を全部 'R' で塗りつぶす
        for x in range(W):
            if mskW & (1 << x):
                for y in range(H):
                    c2[y][x] = 'R'

        # 残っている '#' の数を数える
        cnt = 0
        for y in range(H):
            for x in range(W):
                if c2[y][x] == '#':
                    cnt += 1

        if cnt == K:
            ans += 1

print(ans)

"""
ビット全探索(bit全探索)
hamayanhamayan
https://blog.hamayanhamayan.com/entry/2020/07/05/235310
制約が小さいのでビット全探索で解ける。
選ばれた行と列は赤色で塗りつぶして、黒色部分をカウントしてK個なら答えをインクリメントするといい。

https://atcoder.jp/contests/abc173/tasks/abc173_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6916d04a-2d04-8323-88ce-7d272aa7d788
"""
