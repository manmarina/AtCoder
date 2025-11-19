H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

steps = H + W - 2      # 動く総手数
downs = H - 1          # 下に行く回数

ans = 0

for mask in range(1 << steps):
    # 1 の個数が down と違う mask はスキップ
    if mask.bit_count() != downs:
        continue

    i, j = 0, 0               # (0,0) からスタート（0-index）
    used = {A[0][0]}          # 通った値の集合。最初にスタートを入れておく
    ok = True

    for t in range(steps):
        # t ビット目を見る
        if (mask >> t) & 1:
            # ビットが 1 → 下へ
            i += 1
        else:
            # ビットが 0 → 右へ
            j += 1

        v = A[i][j]
        if v in used:
            ok = False
            break
        used.add(v)

    if ok:
        ans += 1

print(ans)

"""
ビット全探索（bit全探索）
公式解説
組み合わせとしての最大の通り数 18C9（=48620通り）なので全探索可能。
組合せ全探索(combinations)版とほぼ同じコード。

https://atcoder.jp/contests/abc293/tasks/abc293_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/691dbcf5-8c34-8331-86cb-e9ae44683ed5
"""
