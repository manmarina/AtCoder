from itertools import combinations

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

steps = H + W - 2          # 手数
downs = H - 1              # 下に行く回数

ans = 0

for down_pos in combinations(range(steps), downs):
    down_pos = set(down_pos)   # membership が速くなるように set に変換
    i, j = 0, 0                # (0,0) スタート（0-index）
    used = {A[0][0]}           # 通った値の集合

    ok = True
    for t in range(steps):
        if t in down_pos:
            i += 1   # 下へ
        else:
            j += 1   # 右へ

        v = A[i][j]
        if v in used:
            ok = False
            break
        used.add(v)

    if ok:
        ans += 1

print(ans)

"""
組合せ全探索(combinations)
公式解説
組み合わせとしての最大の通り数 18C9（=48620通り）なので全探索可能。

https://atcoder.jp/contests/abc293/tasks/abc293_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/691dbcf5-8c34-8331-86cb-e9ae44683ed5
"""
