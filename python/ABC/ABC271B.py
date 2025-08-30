N, Q = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(N)]
S = [list(map(int, input().split())) for _ in range(Q)]

# print(L)
# print(S)

for sq, tq in S:
    print(L[sq - 1][tq])
