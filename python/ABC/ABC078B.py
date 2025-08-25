X, Y, Z = map(int, input().split())

count = X // (Y + Z)
if X - count * (Y + Z) < Z:
    count -= 1

print(count)
