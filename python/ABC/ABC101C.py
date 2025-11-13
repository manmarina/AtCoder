N, K = map(int, input().split())
A = list(map(int, input().split()))

res = 0
right = 0

while True:
    if res == 0:
        right += K
    else:
        right += (K - 1)

    res += 1

    if right >= N:
        break

print(res)

"""
計算量を削減したシミュレーション
けんちょん
https://drken1215.hatenablog.com/entry/2018/06/24/003500
最初の選択をK通り探索しなくても、片側に寄せて考えると最短の解が得られるというけんちょんのスマートすぎる解!!
もはや配列Aに触れてすらいない。。。

https://atcoder.jp/contests/abc101/tasks/arc099_a
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69158816-b990-8321-b1fc-f05db9ea5cb6
"""
