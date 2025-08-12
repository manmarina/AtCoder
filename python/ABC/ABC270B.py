X, Y, Z = map(int, input().split())

if 0 < Y < X < Z or 0 < Y < Z < X or X < Z < Y < 0 or Z < X < Y < 0:
    print(-1)
elif X < Y < 0 < Z or Z < 0 < Y < X:
    print(2 * abs(Z) + abs(X))
else:
    print(abs(X))
