H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = 0
used = set()  # これまで通ったマスの値の集合


def dfs(i, j):
    global ans

    # そのマスの値がすでに出ていたら、この経路はNG
    if A[i][j] in used:
        return

    # このマスの値を使ったことにする
    used.add(A[i][j])

    # ゴールに着いたら、条件を満たす経路 1 本発見
    if i == H - 1 and j == W - 1:
        ans += 1
    else:
        # 下に行けるなら下へ
        if i + 1 < H:
            dfs(i + 1, j)
        # 右に行けるなら右へ
        if j + 1 < W:
            dfs(i, j + 1)

    # 帰りがけに元に戻す（バックトラック）
    used.remove(A[i][j])


dfs(0, 0)
print(ans)

"""
再帰DFS
公式解説
組み合わせとしての最大の通り数 18C9（=48620通り）なので全探索可能。

https://atcoder.jp/contests/abc293/tasks/abc293_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/691dbcf5-8c34-8331-86cb-e9ae44683ed5
"""
