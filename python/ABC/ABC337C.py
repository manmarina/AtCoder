n = int(input())
G = [0] * (n + 1)  # n+1必要
a = list(map(int, input().split()))  # 自分のインデックス -> 一つ前のインデックス
# print(a)

for i in range(n):
    if a[i] == -1:  # 値が-1のとき
        root = i + 1  # インデックスをスタートに
    else:
        G[a[i]] = i + 1  # 一つ前のインデックス ->自分の（=次の）インデックス
# print(G)

ans = [root]  # スタートのインデックスを追加
i = root
for _ in range(n - 1):
    ans.append(G[i])  # 次のインデックスを追加してゆく
    i = G[i]  # iを更新
print(*ans)

"""
逆順列
A -> G 逆順列を生成して出力。
A:自分のインデックス -> 一つ前のインデックス
G:一つ前のインデックス ->自分の（=次の）インデックス

プロひろ
https://programming-hiroba.com/abc337-c/
DFSで解いている。
DFSに使うグラフに逆順列を使っていた。
DFSしなくても逆順列で答えが得られそうだったのでヒントになった。

https://atcoder.jp/contests/abc337/tasks/abc337_c
"""
