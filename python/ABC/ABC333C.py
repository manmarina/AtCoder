from itertools import product


N = int(input())

repunit = [
    1,
    11,
    111,
    1_111,
    11_111,
    111_111,
    1_111_111,
    11_111_111,
    111_111_111,
    1_111_111_111,
    11_111_111_111,
    111_111_111_111  # 入力例3において、上限のN=333が12桁だったので
]

trio = set()
for r in product(repunit, repeat=3):
    trio.add(sum(r))
trio = sorted(trio)

# print(trio)
print(trio[N - 1])

"""
全探索
リトライ
12 桁以下のトリレプユニット数を列挙する
それらの 3 つの和で表される数を重複なしで列挙する
そのうちの N番目の数を求める

けんちょん
https://drken1215.hatenablog.com/entry/2024/11/02/190153

https://atcoder.jp/contests/abc333/tasks/abc333_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690c454e-dc18-8321-8196-a41fb9edb5f7
"""
