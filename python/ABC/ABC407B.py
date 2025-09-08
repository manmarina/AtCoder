X, Y = map(int, input().split())

count = 0
for i in range(1, 6 + 1):
    for j in range(1, 6 + 1):
        ok = i + j >= X or abs(i - j) >= Y
        if ok:
            count += 1
# print(count)
print(count / 36)
