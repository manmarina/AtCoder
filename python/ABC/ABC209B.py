N, X = map(int, input().split())
A = list(map(int, input().split()))

cost = 0
for i, a in enumerate(A, start=1):  # 1始まりに注意
    if i % 2 == 0:
        cost += a - 1
    else:
        cost += a
print("Yes" if cost <= X else "No")
