N = int(input())
B = list(map(int, input().split()))

A = [B[0]]
# print(A)
for i in range(1, N - 1):
    A.append(min(B[i - 1], B[i]))  # A[i] = min(B[i-1], B[i])
A.append(B[-1])  # 最後の一つはBの最後の一つと同じ値

# print(A)
# print(B)
print(sum(A))

"""
場合分け系

ex.
3 3 5 7 7 5 5
3 5 7 9 7 5
Aiの最大値はmin(B[i-1], B[i])であることを見抜く。

けんちょんの解説
https://drken1215.hatenablog.com/entry/2019/09/16/201500

https://atcoder.jp/contests/abc140/tasks/abc140_c
"""
