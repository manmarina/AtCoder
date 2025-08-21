A, B = map(int, input().split())

for C in range(1, 3 + 1):
    temp = A * B * C
    if temp % 2 == 1:
        print("Yes")
        break
else:
    print("No")
