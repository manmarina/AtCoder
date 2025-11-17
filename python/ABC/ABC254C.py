N, K = map(int, input().split())
A = list(map(int, input().split()))

# Aを同じ余りクラスごとのリストに分割してサブリストとして格納
B = [[] for _ in range(K)]
for i in range(N):
    B[i % K].append(A[i])
# print(B)

# Bのサブリストをソート
for i in range(len(B)):
    B[i].sort()
# print(B)

# Bのサブリストを再度結合
C = []
for i in range(N):
    C.append(B[i % K][i // K])
# print(C)

# 昇順になっているか判定
for i in range(N - 1):
    if C[i] > C[i + 1]:
        print("No")
        exit()

print("Yes")

"""
基本実装問題
リトライ
操作で交換できるのは「距離が K の倍数」のペアだけ＝同じ余りクラス内。

https://atcoder.jp/contests/abc254/tasks/abc254_c
"""
