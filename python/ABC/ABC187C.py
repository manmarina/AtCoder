N = int(input())
S = [input() for _ in range(N)]
# print(S)

set_ = set(S)
for s in S:
    tex = '!' + s
    if tex in set_:
        print(s)
        exit()
print("satisfiable")

"""
文字列処理 + 集合(set)・ハッシュ

不憫な文字列の定義を読み誤らない。
不憫な文字列とは、
    a -> a, !aの両方存在
    !a -> !a, !!aの両方存在

https://atcoder.jp/contests/abc187/tasks/abc187_c
https://chatgpt.com/g/g-p-688d3155796881919ed997146b54eec1-atcoder/c/68f99a43-11e0-8322-be68-20ac8f0b9b1c
"""
