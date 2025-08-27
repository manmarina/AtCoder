A, B, K = map(int, input().split())

A_rem = max(0, A - K)
eat_from_B = max(0, K - A)
B_rem = max(0, B - eat_from_B)
print(A_rem, B_rem)
