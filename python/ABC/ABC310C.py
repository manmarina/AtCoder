N = int(input())
S = set(input() for _ in range(N))
# print(S)

pool = set()  # 削除候補
for s in S:
    if s == s[::-1]:  # 回文はパスする
        continue

    rs = ''.join(s[::-1])  # 文字列を逆順にする
    if rs in S and s not in pool:  # 逆順がSにあったら削除候補にする
        pool.add(rs)

# print(pool)
# print(S)

print(len(S) - len(pool))

"""
文字列操作
反転して同じ文字列なら同じと判断する。
回文を除外するのを忘れないこと。

けんちょん
https://drken1215.hatenablog.com/entry/2025/02/09/023754

https://atcoder.jp/contests/abc310/tasks/abc310_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690c560e-0b80-8321-b5d5-46855a13b20b
"""
