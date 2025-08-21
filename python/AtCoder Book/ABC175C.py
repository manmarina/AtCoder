X, K, D = map(int, input().split())

if abs(X) > K * D:
    print(abs(X) - K * D)
else:
    ta = abs(X) // D
    tb = K - ta
    if tb % 2 == 1:
        ta += 1
    print(abs(abs(X) - D * ta))
