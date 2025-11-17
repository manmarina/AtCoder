import sys
sys.setrecursionlimit(10**7)

h1, h2, h3, w1, w2, w3 = map(int, input().split())
h = [h1, h2, h3]
w = [w1, w2, w3]
# print(h)
# print(w)

# 合計が違う場合は 0
if sum(h) != sum(w):
    print(0)
    exit()

a = [[0] * 3 for _ in range(3)]
ans = 0


def dfs(ij):
    global ans
    i, j = divmod(ij, 3)

    # 3x3 すべて埋まった
    if i == 3:
        ans += 1
        return

    # 最終行（i == 2）のときは列の合計から決め打ち
    if i == 2:
        x = w[j] - a[0][j] - a[1][j]
        if x <= 0:
            return
        a[i][j] = x
        dfs(ij + 1)

    # 最終列（j == 2）のときは行の合計から決め打ち
    elif j == 2:
        x = h[i] - a[i][0] - a[i][1]
        if x <= 0:
            return
        a[i][j] = x
        dfs(ij + 1)

    # それ以外のマスは 1〜30 を全探索
    else:
        for x in range(1, 31):
            a[i][j] = x
            dfs(ij + 1)


dfs(0)
print(ans)

"""
工夫して探索の通り数を減らす全探索 DFS版
公式

数独・ナンプレ風問題
3x3 の正の整数マスに行和 H1,H2,H3 と列和 W1,W2,W3 を合わせる「個数を数える」課題です。

https://atcoder.jp/contests/abc256/tasks/abc256_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/691b1ce1-0a44-8321-928e-308788e947cf
"""
