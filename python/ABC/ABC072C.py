N = int(input())
A = list(map(int, input().split()))

MAX = 100_001  # aiの制約の上限
nums = [0] * MAX  # ai -> 個数
for a in A:
    nums[a] += 1

res = 0
for x in range(1, MAX - 1):  # Xを1〜最大値まで試す
    num = nums[x - 1] + nums[x] + nums[x + 1]
    res = max(res, num)  # x-1の個数 + xの個数 + X+1の個数が最大なら更新

print(res)

"""
工夫して探索の通り数を減らす全探索
aiの増減を全探索するのではなく、増減後の数値Xを全探索する。

けんちょん
https://drken1215.hatenablog.com/entry/2024/11/09/152008
問題文では操作後に整数値 Xを選んでいるが、整数値 Xを先に選んでから操作しても、一向に構わない。

そこで、整数値 Xを仮決めしたときに、数列をどのように操作すれば良いかを考えてみよう。
少し考えると、次のように結論付けられる。

Ai=Xのとき：何もしない
Ai=X-1のとき：1 を足す
Ai=X+1のとき：1 を引く
Aiの値がそれ以外のとき：どうしようもない（Xには一致させられない）

このことから、Xを決めたときのスコアは次のようになる。

Ai=X-1,X,X+1となるような iの個数。
これを効率よく求めるために、次のバケットを用意しよう。

nums[x]：ai -> 個数

https://atcoder.jp/contests/abc072/tasks/arc082_a
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69140b13-9334-8321-b54c-4b8c35f7850b
"""
