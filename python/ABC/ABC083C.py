X, Y = map(int, input().split())

res = 0
num = X

# 値が Y を超えるまで 2 倍し続ける
while num <= Y:
    res += 1  # カウントする
    num *= 2

print(res)

"""
問題文の理解が難解系
一般に、Aiが決まっているとき、Ai+1=2Aiとすればよい。
こうして、Yを超えるまで続けていけばよい。

けんちょん
https://drken1215.hatenablog.com/entry/2025/01/29/130009

https://atcoder.jp/contests/abc083/tasks/arc088_a
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690a9984-be04-8321-a38a-476ed262f247
"""
