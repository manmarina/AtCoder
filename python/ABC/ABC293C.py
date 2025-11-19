H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

steps = H + W - 2          # 手数
downs = H - 1              # 下に行く回数

ans = 0
path = []


def dfs(start, depth):
    global cnt

    if depth == 0:  # 完成したら
        # print(tuple(path))
        path_chk(path)
        return

    for i in range(start, steps):  # 範囲を設定
        path.append(i)
        dfs(i + 1, depth - 1)  # 次の深さへ
        path.pop()  # 戻す（バックトラッキング）


def path_chk(path):
    global ans
    down_pos = set(path)

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


dfs(0, downs)
print(ans)

"""
組合せ全探索(combinations) + 再帰DFS
公式解説
組み合わせとしての最大の通り数 18C9（=48620通り）なので全探索可能。

https://atcoder.jp/contests/abc293/tasks/abc293_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/691dbcf5-8c34-8331-86cb-e9ae44683ed5
"""
