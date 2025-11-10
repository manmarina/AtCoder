X, Y = map(int, input().split())

cnt = 0
while X <= Y:
    X *= 2
    cnt += 1
print(cnt)

"""
問題文の理解が難解系
リトライ
一般に、A[i]が決まっているとき、A[i+1]=2A[i]とすればよい。
こうして、Yを超えるまで続けていけばよい。

けんちょん
https://drken1215.hatenablog.com/entry/2025/01/29/130009

https://atcoder.jp/contests/abc083/tasks/arc088_a
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690a9984-be04-8321-a38a-476ed262f247
"""
