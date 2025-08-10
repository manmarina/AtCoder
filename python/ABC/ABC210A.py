N, A, X, Y = map(int, input().split())

if N <= A:
    total = N * X
else:
    total = X * A
    total += Y * (N - A)

print(total)
