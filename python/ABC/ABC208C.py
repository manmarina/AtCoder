N, K = map(int, input().split())
A = [[v, i]
     for i, v in enumerate(map(int, input().split()))]  # (国民番号, index)のリストを作成
A.sort()  # 国民番号でソート
# print(A)

for i in range(N):
    A[i][0] = i  # 国民番号をランクに置き換え
# print(A)

dic = {}
for i in range(N):
    v, i = A[i]
    dic[i] = v  # key=index,value=ランク
# print(dic)

div, mod = divmod(K, N)  # div=全員が受け取れる数,mod=ランクがmod未満の人が受け取る総数
# print(div, mod)

for i in range(N):
    if dic[i] < mod:  # ランクがmod未満なら
        print(div + 1)  # 余りを受け取る
    else:
        print(div)  # 余りを受け取れない

"""
バケットと連想配列
連想配列を活用して、index->ランクをO(1)で取り出す。

https://atcoder.jp/contests/abc208/tasks/abc208_c
"""
