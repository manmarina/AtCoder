A, B, C, X, Y = map(int, input().split())


def is_AB_lower(A, B, C):
    if A + B > 2 * C:
        return True
    else:
        return False


def buy_A_and_B(A, B, X, Y):
    total = A * X + B * Y
    return total


def buy_AB(A, B, C, X, Y):
    if X < Y:
        total = C * 2 * X
        rest = Y - X
        if B > C * 2:
            total += C * 2 * rest
        else:
            total += B * rest
    else:
        total = C * 2 * Y
        rest = X - Y
        if A > C * 2:
            total += C * 2 * rest
        else:
            total += A * rest
    return total


if is_AB_lower(A, B, C):
    print(buy_AB(A, B, C, X, Y))
else:
    print(buy_A_and_B(A, B, X, Y))
