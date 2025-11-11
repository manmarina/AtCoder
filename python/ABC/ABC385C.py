N = int(input())
H = list(map(int, input().split()))

res = 1

# 数列の間隔 d を全探索
for d in range(1, N):
    # 数列全体を d 個に分割して解く
    for r in range(d):
        num = 1
        prev = -1
        # 分割して得られた数列に対して、同じ値が最大何個連続しているかを求める
        for i in range(r, N, d):
            if H[i] == prev:
                num += 1
                res = max(res, num)
            else:
                num = 1
                prev = H[i]

print(res)

"""
工夫して探索の通り数を減らす「全探索 + 枝刈り」
けんちょん
https://drken1215.hatenablog.com/entry/2024/12/25/021000
このように数列を分けると、各数列に対して次の問題を考えればよいことになる。
与えられた数列において、同じ値が最大で何個連続しているかを求めよ。
この問題は、数列の長さを Lとして、O(L)の計算量で解ける。

d個の数列の長さの総和は Nであるから、結局、d個の数列について上記の問題を解くのに要する計算量は O(N)と評価できる。
dが O(N)通りあるから、全体の計算量は O(N2)と評価できる。

https://atcoder.jp/contests/abc385/tasks/abc385_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69135f68-9700-8321-972a-894de77cbdaf
"""
