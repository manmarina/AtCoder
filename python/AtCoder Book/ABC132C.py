N = int(input())
d = list(map(int, input().split()))

d.sort()

if len(d) % 2:
    print(0)
else:
    print(d[len(d) // 2] - d[len(d) // 2 - 1])
