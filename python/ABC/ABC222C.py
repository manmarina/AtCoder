N, M = map(int, input().split())
A = [0] + [input() for _ in range(2 * N)]
rankl = [i for i in range(1, 2 * N + 1)]  # ランキングリスト
rankd = {i: 0 for i in range(1, N * 2 + 1)}  # ランキングリストを作成するための辞書
# print(A)
# print(rankl)
# print(rankd)


def janken(jk1, jk2):  # じゃんけんを判定する関数
    if jk1 == jk2:
        return 0
    if (jk1, jk2) in (('G', 'C'), ('C', 'P'), ('P', 'G')):
        return 1
    else:
        return 2


for j in range(M):
    # (1,2),(3,4)...の順に取り出し、(1,2)を対戦、(3,4)を対戦、を繰り返す
    for i in range(0, 2 * N, 2):
        # print(i, i + 1)
        rk1 = rankl[i]  # ランキングリストから取り出す
        jk1 = A[rk1][j]
        rk2 = rankl[i + 1]  # ランキングリストから取り出す
        jk2 = A[rk2][j]
        # print(jk1, jk2)

        res = janken(jk1, jk2)
        if res == 1:  # jk1が勝ったら
            rankd[rk1] += 1
        elif res == 2:  # jk2が勝ったら
            rankd[rk2] += 1
        # print(rankd)

        # ランキング辞書をソートしてランキングリストを作成
        rankl = sorted(rankd.keys(), key=lambda k: (-rankd[k], k))
        # print(rankl)

print(*rankl, sep='\n')

"""
シミュレーション系
自力解

やることは「じゃんけん総当たりのスイス式トーナメント」を素直にシミュレーションするだけです。
必要テク：シミュレーション／安定ソート（多キーソート）／実装の丁寧さ。

対戦相手の決定ロジックがわかりにくい！！
    まず勝ち数順、その次にインデックス順にソートしたランキングリストを作成
    そのランキングリストの1-2位、3-4位...の順で対戦する

何をする問題？
    参加者は 2N 人、各人は 長さ M の手の列（各ラウンドで出す手）を持つ。
    ラウンドごとに、現在の順位順に上から (0 vs 1), (2 vs 3), ... と対戦。
    勝ったら勝数 +1、あいこは増えない。
    ラウンド終了後に、勝数の降順→元の番号の昇順で並べ替え、次ラウンドの組み合わせを作る。
    M ラウンド後の最終順位を出力。
"""
