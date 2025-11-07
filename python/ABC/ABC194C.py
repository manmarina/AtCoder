N = int(input())
A = list(map(int, input().split()))

s = sum(A)
s2 = sum(x * x for x in A)

ans = N * s2 - s * s
print(ans)

"""
数学的気づき系
数列の式を変形して解をO(N)で計算できる式を導く。
チャッピーが展開してくれた式変形を理解できるように頑張ろう！！

https://atcoder.jp/contests/abc194/tasks/abc194_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/690e0b82-d200-8324-98e3-44a1db80f6dd
"""
