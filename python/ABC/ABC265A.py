X, Y, N = map(int, input().split())


if Y > X * 3:
    total = X * N
else:
    Y_count = N // 3
    Y_total = Y * Y_count
    X_count = N % 3
    X_total = X * X_count
    total = Y_total + X_total

print(total)
