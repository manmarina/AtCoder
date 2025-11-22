N, M = map(int, input().split())
E = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    E[a][b] = c  # 通常の隣接リストではなく、インデックス=隣接頂点、値=長さであることに注意
    E[b][a] = c
# print(E)

ans = 0
used = [False] * (N + 1)


def dfs(v, s):  # 頂点番号だけでなく、長さの合計も渡す
    global ans
    used[v] = True
    if s > ans:
        ans = s  # 長さが最長の時更新する
    for i in range(1, N + 1):
        if not used[i] and E[v][i]:  # E[v][i]が0でないことが前提
            dfs(i, s + E[v][i])  # 頂点番号だけでなく、長さの合計も渡す
    used[v] = False  # バックトラック


for i in range(1, N + 1):  # すべての頂点からスタート
    dfs(i, 0)

print(ans)

"""
再帰DFSによる全探索
公式解説
各頂点をスタートとして DFS
訪問済み管理（bit or visited 配列）をしながら、
行けるところまで行っては戻る（バックトラック）
その中で重み合計の最大値を更新
という「深さ優先探索＋バックトラック」が本筋です

https://atcoder.jp/contests/abc317/tasks/abc317_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69216c06-d020-8324-aee8-e12e0e4599cb
"""
