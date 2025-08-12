X, Y, Z = map(int, input().split())


if 0 < X:
    if Y < 0 or X < Y:
        print(X)
    elif Y < Z:
        print(-1)
    elif Z > 0:
        print(X)
    else:
        print(X - (Z * 2))
else:
    if Y > 0 or X > Y:
        print(-X)
    elif Y > Z:
        print(-1)
    elif Z < 0:
        print(-X)
    else:
        print(- X + (Z * 2))
