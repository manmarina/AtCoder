# --- 解法1: 1本外し + 連結判定 ---
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


def is_connected_without(edge_index: int) -> bool:
    """edges[edge_index] を無視したときに全頂点が連結か？"""
    a, b = edges[edge_index]
    seen = [False] * N
    st = [0]  # 0番から開始（もともと連結なので基準はどこでもOK） st=stack
    seen[0] = True
    while st:
        u = st.pop()
        for v in G[u]:
            # 取り除いた道路の場合はスキップ
            if (u == a and v == b) or (u == b and v == a):
                continue
            if not seen[v]:
                seen[v] = True
                st.append(v)
    return all(seen)


ans = 0
for i in range(M):
    if not is_connected_without(i):
        ans += 1
print(ans)

"""
反復DFS（スタックを使用）

全探索（辺を1本ずつ外して連結判定）
各辺(e)を1本だけ無視して、DFS/BFSで到達できる頂点数を数える
全頂点に到達できなければ、その e は橋
"""
