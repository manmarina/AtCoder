X, Y = map(int, input().split())

ok = 0
for x in range(1, 7):
    for y in range(1, 7):
        if (x + y >= X) or (abs(x - y) >= Y):
            ok += 1

print(ok / 36.0)
