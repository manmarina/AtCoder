N = int(input())
A = list(map(int, input().split()))
B = []
for i in range(1, N + 1):
    B.append((A[i - 1], i))  # (登校した順番、生徒番号)のリストを作成
B.sort()  # 登校した順番でソート
# print(B)

for i in range(N):
    print(B[i][1], end=' ')  # 投稿した順に生徒番号を出力
print()

"""
逆順列
いわゆる逆順列を求める問題。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2019/10/03/003600

https://atcoder.jp/contests/abc142/tasks/abc142_c/editorial
"""
