H, W = map(int, input().split())
G = [input() for _ in range(H)]
# print(G)


def is_outside(x, y):
    if not 0 <= x < H or not 0 <= y < W:
        return True
    return False


i = 0
j = 0
visited = set()  # 訪問管理するset
while True:
    if (i, j) in visited:  # ループ検出して終了
        print("-1")
        exit()
    visited.add((i, j))  # 現在の座標をsetに追加

    # コンベア移動して壁なら終了
    if G[i][j] == 'U':
        if is_outside(i - 1, j):
            print(i + 1, j + 1)
            exit()
        i -= 1
    elif G[i][j] == 'D':
        if is_outside(i + 1, j):
            print(i + 1, j + 1)
            exit()
        i += 1
    elif G[i][j] == 'L':
        if is_outside(i, j - 1):
            print(i + 1, j + 1)
            exit()
        j -= 1
    else:  # G[i][j] == 'R':
        if is_outside(i, j + 1):
            print(i + 1, j + 1)
            exit()
        j += 1

"""
カーソル系
以前に解いているのに気づかずにもう一度解いた

https://atcoder.jp/contests/abc265/tasks/abc265_c
"""
