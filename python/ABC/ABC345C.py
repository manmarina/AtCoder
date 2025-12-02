from collections import Counter


S = input()

can_S = 0
cnt = Counter(S)
# print(cnt)


def nC2(num):
    return num * (num - 1) // 2


ans = nC2(len(S))
# print(ans)

for v in cnt.values():
    if v > 1:
        can_S = 1  # 同じ文字が出現するときは、入れ替えても同じ並びになるという1パターンが存在する
        ans -= nC2(v)
print(ans + can_S)  # 同じ文字が出現するときは、1つ加算する

"""
計算量を削減したシミュレーション
修正
けんちょん
https://drken1215.hatenablog.com/entry/2024/09/04/015546
操作によってできるものの個数を数え上げる系の問題の最も基本的な問題！

https://atcoder.jp/contests/abc345/tasks/abc345_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/692e74dd-60c0-8320-857d-a4db22cff847
"""
