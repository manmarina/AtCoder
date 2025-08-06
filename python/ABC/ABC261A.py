L1, R1, L2, R2 = map(int, input().split())

L_max = max(L1, L2)
R_min = min(R1, R2)

length = R_min - L_max
if length < 0:
    length = 0

print(length)
