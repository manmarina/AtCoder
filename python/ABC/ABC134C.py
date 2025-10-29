N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
# print(A)

B = sorted(A)  # 2番目に大きい数を知りたいのでソート
for a in A:
    if B[-1] == a:  # aが最大値の場合
        print(B[-2])  # Bの2番目に大きい数
    else:  # そうでないとき
        print(B[-1])  # Bの最大値

"""
場合分け系

けんちょんの解説
https://drken1215.hatenablog.com/entry/2020/12/25/172300
Aiが最大値のときと、そうでないときの場合で考える。

https://atcoder.jp/contests/abc134/tasks/abc134_c
"""
