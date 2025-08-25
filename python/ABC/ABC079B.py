N = int(input())

a, b = 2, 1        # a=L0, b=L1
for _ in range(N):
    a, b = b, a + b
print(a)            # ループ後のaがL_N
