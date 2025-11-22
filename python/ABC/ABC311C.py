import sys
sys.setrecursionlimit(1 << 25)  # 再帰上限の設定を忘れない（わすれたらRE）

N = int(input())
A = list(map(int, input().split()))

G = [0]
for i in range(N):
    G.append(A[i])
# print(G)


def dfs(n):
    if n in path_set:  # TLEを防ぐため判定はsetで
        x = path.index(n)
        path2 = path[x:]  # 閉路部分のみを切り抜く
        print(len(path2))  # 閉路部分の長さを出力
        print(*path2)  # 　閉路の頂点番号を出力
        exit()
    path.append(n)
    path_set.add(n)

    visited[G[n]] = True
    dfs(G[n])
    return


# DFS
visited = [False] * (N + 1)

for i in range(1, N + 1):
    if visited[i]:  # 一度訪問した接続はパス
        continue
    path = []  # 経路を格納
    path_set = set()  # TLEを防ぐためsetも用意する
    visited[i] = True
    dfs(i)
# print(visited)

"""
DFS
サイクル検出の問題。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2023/07/24/030543
https://drken1215.hatenablog.com/entry/2023/05/20/200517

https://atcoder.jp/contests/abc311/tasks/abc311_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69212e6e-d978-8321-a3b8-304a11f76e83
"""
