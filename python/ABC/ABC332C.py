N, M = map(int, input().split())
S = input()

for i in range(1001):  # ロゴTシャツ0枚から試してゆく
    mujiT = M  # 無地Tシャツを持っている枚数
    mujiT_dirt = 0  # 汚れた無地Tシャツの枚数
    logoT = i  # ロゴTシャツを持っている枚数
    logoT_dirt = 0  # 汚れたロゴTシャツの枚数
    for s in S:
        if s == '1':  # 無地Tから優先して着る 着れなかったら次のループに行く
            if mujiT - mujiT_dirt > 0:
                mujiT_dirt += 1
            elif logoT - logoT_dirt > 0:
                logoT_dirt += 1
            else:
                break
        elif s == '2':  # ロゴTを着る 着れなかったら次のループに行く
            if logoT - logoT_dirt > 0:
                logoT_dirt += 1
            else:
                break
        else:  # s == '0': # 洗濯して全てキレイになる
            mujiT_dirt = 0
            logoT_dirt = 0
    else:
        print(i)
        exit()

"""
シミュレーション
制約が小さいので、Tシャツを1枚も買っていない状態から試す。
だめなら1枚買って試すのを繰り返す。うまく行ったときの枚数が答え。

https://atcoder.jp/contests/abc332/tasks/abc332_c
"""
