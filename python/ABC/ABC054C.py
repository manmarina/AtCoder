import sys
sys.setrecursionlimit(1 << 25)  # ただの“非常に大きい数（＝保険）”としての慣習値

# グラフは隣接リストで管理
N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

seen = [False] * N


def dfs(v):
    # C++版の end 判定：v 以外がすべて訪問済みならカウント
    if all(seen[i] or i == v for i in range(N)):
        return 1

    seen[v] = True

    # 以下は下のコードと完全に同義
    res = 0
    for nv in G[v]:
        if seen[nv]:
            continue
        res += dfs(nv)
    seen[v] = False  # 戻す（バックトラック）
    return res


# def dfs(v):  # 比較 最初にvを訪問済みにするほうがわかりやすい
#     seen[v] = True
#     if all(seen):          # 全頂点訪問
#         seen[v] = False
#         return 1

#     # 以下は上のコードと完全に同義
#     res = 0
#     for nv in G[v]:
#         if not seen[nv]:
#             res += dfs(nv)
#     seen[v] = False        # バックトラック
#     return res


# print(G)
# print(seen)
print(dfs(0))

"""
DFS（深さ優先探索）
再帰関数による実装
けんちょんの実装をPythonに移植

問題タイプ：小規模グラフでの全列挙（順列/DFS）
目的：頂点1から出発し、全頂点を一度ずつ訪れる道（=ハミルトン路）で、隣接する頂点同士が辺で結ばれているものの個数を数える。
"""
