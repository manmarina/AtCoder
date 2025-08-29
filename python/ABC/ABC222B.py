N, P = map(int, input().split())
a = list(map(int, input().split()))

count = 0
for point in a:
    if point < P:
        count += 1
print(count)
