X, Y = map(int, input().split())

for x in range(X + 1):
    y = X - x
    if 2 * x + 4 * y == Y:
        print("Yes")
        break
else:
    print("No")
