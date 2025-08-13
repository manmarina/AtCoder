N, X, T = map(int, input().split())

if N % X:
    print((N // X + 1) * T)
else:
    print((N // X) * T)
