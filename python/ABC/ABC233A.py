X, Y = map(int, input().split())

count = 0
if X < Y:
    diff = (Y-X)
    count = diff // 10
    if diff % 10 > 0:
        count += 1

print(count)
