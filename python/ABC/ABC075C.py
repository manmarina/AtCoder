import sys
sys.setrecursionlimit(1 << 25)

N, M = map(int, input().split())
edges = []
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((a, b))
    G[a].append(b)
    G[b].append(a)


def dfs(u: int, a: int, b: int, seen: list):
    seen[u] = True
    for v in G[u]:
        # 無視する辺ならスキップ
        if (u == a and v == b) or (u == b and v == a):
            continue
        if not seen[v]:
            dfs(v, a, b, seen)   # ← ここで再帰呼び出し


def is_connected_without(edge_index: int) -> bool:
    """edges[edge_index] を無視したときに全頂点が連結か？"""
    a, b = edges[edge_index]
    seen = [False] * N
    dfs(0, a, b, seen)  # 0番から探索開始
    return all(seen)


ans = 0
for i in range(M):
    if not is_connected_without(i):
        ans += 1
print(ans)

"""
再帰DFS

全探索（辺を1本ずつ外して連結判定）
各辺(e)を1本だけ無視して、DFS/BFSで到達できる頂点数を数える
全頂点に到達できなければ、その e は橋

バックトラック不要
到達できなかった頂点は、そもそもどのルートを使っても到達できない
    例えば seen[x] が最後まで False だったなら、
    DFSで試せるすべての辺（無視していない辺）はたどり済みです。
    別ルートから試す必要があったなら、そのルートも探索のどこかで自然に辿っているはず。

バックトラックが必要になる場合との違い
組合せ探索：
    「ある要素を選ぶ」or「選ばない」という両方を試す必要がある
    だから片方を試したあとに「戻す（バックトラック）」が必須
    ABC054Cはグラフ問題だが「訪問順が異なる経路を全部数える」のでバックトラックが必要

グラフ探索：
    「行けるか行けないか」の事実が確定すれば、それで十分
    「別ルートでも行けるか？」は気にしなくてよい（到達済みならYes、未訪問ならNoで確定）
"""
