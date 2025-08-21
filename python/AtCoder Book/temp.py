def solve():
    N = int(input())

    pt, px, py = 0, 0, 0

    for i in range(N):
        t, x, y = map(int, input().split())
        T, X, Y = t - pt, abs(x - px), abs(y - py)

        if T < X + Y:
            return False

        if T % 2 != (X + Y) % 2:
            return False

        pt, px, py = t, x, y
    return True


print("Yes" if solve() else "No")
