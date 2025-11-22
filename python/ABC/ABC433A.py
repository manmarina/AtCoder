X, Y, Z = map(int, input().split())

for i in range(0, 100 + 1):
    # print(i, X + i, (Y + i) * Z)
    if X + i == (Y + i) * Z:
        print("Yes")
        exit()
print(("No"))
