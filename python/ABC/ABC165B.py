X = int(input())

cur = 100
count = 0
while cur < X:
    cur += cur // 100
    count += 1
print(count)
