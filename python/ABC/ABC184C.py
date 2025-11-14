def solve():
    a, b, c, d = map(int, input().split())
    p = abs(c - a)
    q = abs(d - b)

    if p == 0 and q == 0:  # 同じ座標は0手
        print(0)
        return

    if p == q or p + q <= 3:  # 斜めのライン上か、マンハッタン距離が3未満は1手
        print(1)
        return

    # マンハッタン距離が偶数のとき、マンハッタン距離が6以内は2手 abs(p - q) <= 3は理解できない。。
    if (p + q) % 2 == 0 or p + q <= 6 or abs(p - q) <= 3:
        print(2)
        return

    print(3)


solve()

"""
カーソル系 + 場合分け系
けんちょん
https://drken1215.hatenablog.com/entry/2020/11/22/224600
abs(p - q) <= 3が理解できない。。

https://atcoder.jp/contests/abc184/tasks/abc184_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6917197d-a194-8321-8fd9-beb3f2eb173e
"""
