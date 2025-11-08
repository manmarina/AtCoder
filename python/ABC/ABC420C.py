N, Q = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
Query = [list(input().split()) for _ in range(Q)]
# print("A:", A)
# print("B:", B)

min_AB = 0  # min(Ak,Bk)を集計した変数
for i in range(N):
    min_AB += min(A[i], B[i])

for c, x, v in Query:
    x = int(x) - 1  # 0-indexed
    v = int(v)
    if c == 'A':
        min_AB -= min(A[x], B[x])
        A[x] = v
        min_AB += min(A[x], B[x])  # min_ABを更新
        print(min_AB)
    else:  # c == 'B':
        min_AB -= min(A[x], B[x])
        B[x] = v
        min_AB += min(A[x], B[x])  # min_ABを更新
        print(min_AB)

"""
計算量を削減したクエリ処理
min(Ak,Bk)を集計した変数を利用してO(1)で答える。

https://atcoder.jp/contests/abc420/tasks/abc420_c
"""
