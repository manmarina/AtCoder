N, K, Q = map(int, input().split())
A = list(map(int, input().split()))         # 1-index入力を0-indexにしてもOK
L = list(map(int, input().split()))         # 動かす駒の番号（1-index）

# print(A)
# print(L)

for l in L:
    i = l - 1                               # 0-index
    if A[i] == N:                           # 右端なら動けない
        continue
    if i == K - 1 or A[i] + 1 < A[i + 1]:   # 右隣が離れているなら動ける
        A[i] += 1

# print(A)
# print(*A)
