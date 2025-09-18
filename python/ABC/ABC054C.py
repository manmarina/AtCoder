import sys
sys.setrecursionlimit(1 << 25)

# グラフはけんちょんのコードと同じ
N, M = map(int, input().split())
adj = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    adj[a].append(b)
    adj[b].append(a)

ALL = (1 << N) - 1


def dfs(v, mask):
    if mask == ALL:  # 全頂点訪問
        return 1
    res = 0
    for nx in adj[v]:
        if (mask >> nx) & 1 == 0:
            res += dfs(nx, mask | (1 << nx))  # 変更して渡している 関数冒頭で変更しても良い
    return res


print(dfs(0, 1 << 0))  # 頂点0(=1)から開始

"""
DFS（深さ優先探索）
再帰関数による実装
チャッピー
seen配列をビットマスクに変更
ビットマスクは引数渡しなのでバックトラック不要

問題タイプ：小規模グラフでの全列挙（順列/DFS）
目的：頂点1から出発し、全頂点を一度ずつ訪れる道（=ハミルトン路）で、隣接する頂点同士が辺で結ばれているものの個数を数える。
"""
