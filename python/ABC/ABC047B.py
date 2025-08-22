W, H, N = map(int, input().split())

L, R = 0, W
B, T = 0, H

for _ in range(N):
    x, y, a = map(int, input().split())
    if a == 1:
        L = max(L, x)
    elif a == 2:
        R = min(R, x)
    elif a == 3:
        B = max(B, y)
    else:  # a == 4
        T = min(T, y)

width = max(0, R - L)
height = max(0, T - B)
print(width * height)
