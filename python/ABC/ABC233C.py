N, X = map(int, input().split())
A = []
for _ in range(N):
    _, *a = map(int, input().split())
    A.append(a)
print(A)

ans = 0


def dfs(i, rem):
    global ans
    if i == N:  # 袋がなくなった時（最後の袋の次）
        if rem == 1:  # remが1になっていたら総積がX
            ans += 1  # カウントを+1する
        return
    for a in A[i]:
        if rem % a == 0:  # 割り切れない枝は即捨てる!! < -ここが再帰DFSの良いところ!!
            dfs(i + 1, rem // a)  # 残り目標を更新して次の袋へ


dfs(0, X)
print(ans)

"""
再帰DFSによる全探索
チャッピー

N個の袋（配列）からそれぞれ1個ずつ選ぶ
選んだ数の積がちょうど X になる組合せの数を数える
という問題です。ポイントは「積=X」による強い枝刈りです。

今回の DFS は itertools.product(*L) の手動実装版。
ただし、product だと「割り切れない枝を途中でスキップする」ような枝刈りができないため、
条件がある場合は DFS のほうが効率的です。

今回のグラフは木なのでvisited配列による訪問管理不要。
    グラフ = 一般的なネットワーク（閉路あり得る）
    木 = 閉路のない特別なグラフ（一本道しかない）

https://atcoder.jp/contests/abc232/tasks/abc232_c
https://chatgpt.com/c/68d35598-a048-8321-bca7-7d86319d11ac
"""
