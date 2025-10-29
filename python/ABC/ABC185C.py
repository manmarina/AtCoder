L = int(input())

# nCrを求めている（n=L-1, r=11)
res = 1
for i in range(1, 12):
    res *= L - i
    res //= i

print(res)

"""
数学的な気づき系
けんちょん
https://drken1215.hatenablog.com/entry/2020/12/14/015500
二項係数（nCr）を求める問題。

pythonなら
import math
print(math.comb(L-1, 11))
でも求められる。

https://atcoder.jp/contests/abc185/tasks/abc185_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/6901818d-7e14-8324-a757-693eb3b2cb65
"""
