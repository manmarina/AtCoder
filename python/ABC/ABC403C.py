N, M, Q = map(int, input().split())

perm = [set() for _ in range(N + 1)]

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        _, x, y = q
        perm[x].add(y)
    elif q[0] == 2:
        _, x = q
        perm[x].add("all")  # O(1)で追加できるように改善
    else:  # q[0] == 3
        _, x, y = q
        if y in perm[x] or "all" in perm[x]:  # "all"がある場合のチェックを追加
            print("Yes")
        else:
            print("No")

"""
計算量を削減したクエリ処理
TLE -> AC

すべてのページの閲覧権限を愚直に追加するとO(M)なので、全体でO(QM)となりTLE
そこで、"all"というフラグを追加してO(1)に改善、全体でO(Q)となりAC

https://atcoder.jp/contests/abc403/tasks/abc403_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68f9bda9-6bb8-8321-983e-2de1061f5bb7
"""
