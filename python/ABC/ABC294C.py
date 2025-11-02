N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

At = []
for i in range(N):
    At.append((A[i], 'A'))  # Aの要素にAのスタンプを押して格納。
# print(At)

Bt = []
for i in range(M):
    Bt.append((B[i], 'B'))  # Bの要素にBのスタンプを押して格納
# print(Bt)

C = At + Bt  # A,Bを連結して
C.sort()  # ソート
# print(C)

Al = []
Bl = []
for i in range(N + M):
    _, t = C[i]
    if t == 'A':  # スタンプがAの時
        Al.append(i + 1)  # Aの順位リストに順位を格納
    else:  # t == 'B': # スタンプがBの時
        Bl.append(i + 1)  # Bの順位リストに順位を格納

print(*Al)
print(*Bl)

"""
基本実装問題
2つの数列を連結する。連結後の数列の順位を連結前の並びで出力する。

https://atcoder.jp/contests/abc294/tasks/abc294_c
"""
