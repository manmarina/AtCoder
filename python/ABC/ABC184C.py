a, b = map(int, input().split())
c, d = map(int, input().split())


def count(a, b, c, d):
    # 同じ座標は0手
    if a == c and b == d:
        return 0

    # 斜めのライン上は1手
    if a + b == c + d or a - b == c - d:
        return 1

    # マンハッタン距離が3未満は1手
    if abs(a - c) + abs(b - d) <= 3:
        return 1

    # マンハッタン距離が偶数のときは2手
    if (abs(a - c) + abs(b - d)) % 2 == 0:
        return 2

    # 斜めラインの隣のときは2手
    if a - b == (c - 1) - d or a - b == c - (d - 1) or \
            a + b == (c - 1) + d or a + b == c + (d - 1):
        return 2

    # そうでないとき(マンハッタン距離が奇数）のときは3手
    return 3


print(count(a, b, c, d))

"""
カーソル系 + 数学的な気づき系
WA
「2手で行ける範囲」 を十分にカバーしきれていないこと。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2020/11/22/224600
偶奇を考える。

https://atcoder.jp/contests/abc184/tasks/abc184_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6917197d-a194-8321-8fd9-beb3f2eb173e
"""
