N = int(input())
AB = [tuple(map(int, input().split())) for _ in range(N)]

count = 0
for a, b in AB:
    if a < b:
        count += 1

print(count)
