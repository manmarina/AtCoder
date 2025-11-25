N, D, P = map(int, input().split())
F = list(map(int, input().split()))

F.sort(reverse=True)
# print(F)

cost = 0
for i in range(0, N, D):
    # print(i, i + D)
    bulk = sum(F[i:i + D])
    if bulk > P:
        cost += P
    else:
        cost += bulk
print(cost)

"""
貪欲法
めずらしく簡単な問題。
降順にソートして、周遊券の日数分の通常合計運賃と、周遊券価格を比較。
周遊券がオトクなら買うだけの問題。

https://atcoder.jp/contests/abc318/tasks/abc318_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6925572a-d7f0-8322-89fc-57237188f927
"""
