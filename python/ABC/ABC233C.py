import sys

input = sys.stdin.readline
N, X = map(int, input().split())
L = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    l, arr = tmp[0], tmp[1:]
    L.append(arr)

ans = 0


def dfs(i, rem):
    nonlocal ans
    if i == N:
        if rem == 1:
            ans += 1
        return
    for a in L[i]:
        if rem % a == 0:              # 割り切れない枝は即捨てる
            dfs(i + 1, rem // a)      # 残り目標を更新して次の袋へ


dfs(0, X)
print(ans)

"""
再帰DFS
チャッピー

N個の袋（配列）からそれぞれ1個ずつ選ぶ
選んだ数の積がちょうど X になる組合せの数を数える
という問題です。ポイントは「積=X」による強い枝刈りです。

今回のグラフは木なのでvisited配列による訪問管理不要。
    グラフ = 一般的なネットワーク（閉路あり得る）
    木 = 閉路のない特別なグラフ（一本道しかない）

https://atcoder.jp/contests/abc232/tasks/abc232_c
https://chatgpt.com/c/68d35598-a048-8321-bca7-7d86319d11ac
"""
