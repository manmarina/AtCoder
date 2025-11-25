K = int(input())

vals = []
for bit in range(1 << 10):  # 0～1023
    val = 0
    # 9,8,...,0 の順にチェック
    for d in range(9, -1, -1):
        if bit & (1 << d):
            val = val * 10 + d
    if val > 0:       # 0 は除外（空集合も {0} も 0 になる）
        vals.append(val)

vals.sort()
print(vals[K - 1])  # K番目を表示
# print(vals)

"""
ビット全探索
けんちょん
https://drken1215.hatenablog.com/entry/2023/09/30/120900
321-like Number は
    9876543210 から、いくつかの桁を「歯抜け」にして作ったもの。
    最大 1022 個しかない。
        2^10 - 2
        何も選ばないケースと、0だけ選んだケースの2つを除く。

https://atcoder.jp/contests/abc321/tasks/abc321_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/69256100-b3f4-832b-b627-e231e0b5865d
"""
