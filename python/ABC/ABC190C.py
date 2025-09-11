N, M = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]
K = int(input())
CD = [list(map(int, input().split())) for _ in range(K)]

# 0-indexに変換
AB = [(a - 1, b - 1) for a, b in AB]
CD = [(c - 1, d - 1) for c, d in CD]

# ビットマスクの通りにボールを更に置く
ans = []
for mask in range(1 << K):
    has = [0] * N  # 皿の初期状態（ボールが乗っていない）
    for j in range(K):
        c, d = CD[j]
        if (mask >> j) & 1:
            has[c] += 1  # ビットマスクが1の時
        else:
            has[d] += 1  # ビットマスクが0の時

    # print(has)

    # 条件を数える
    cnt = 0
    for a, b in AB:
        if has[a] and has[b]:  # a,b両方にボールが乗っていたら
            cnt += 1
    ans.append(cnt)

# print(ans)
print(max(ans))

"""
ビット全探索（2^K）
    mask の j ビット目が 0 なら「その人は C_j を選ぶ」、1 なら「D_j を選ぶ」と決める。
    これで全員の選択が一意に定まり、各パターンを評価できます。
    ループは for mask in range(1 << K):。

状態の表現（皿に玉が置かれたか）
    皿は 1..N（入力は1-indexed）なので、0-index に直して has = [0]*N などの配列で管理すると速いです。
    has[x] = 1 にしていき、最後に条件 (A_i, B_i) を走査して has[A_i] and has[B_i] を数えるだけ。

インデックス注意（1-index → 0-index）
    AtCoderの多くの問題と同じく、入力は 1 始まり。内部では -1 して扱うとバグりにくいです。

計算量見積もり
    各 mask で K 回（皿に置く処理）＋ M 回（条件チェック）。
    合計は O( (K+M) · 2^K )。K ≤ 16, M ≤ 100 なので余裕。

実装の小技
    皿配列の再初期化を毎回やってOK（N ≤ 100 で軽い）。
    もっと詰めるなら、chosen = [C_j or D_j] を作ってから has を立てる。
    itertools.product((0,1), repeat=K) を使っても良いですが、ビットの方が軽量・定番です。
"""
