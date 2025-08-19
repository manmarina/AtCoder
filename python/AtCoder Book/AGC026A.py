N = int(input())
a = list(map(int, input().split()))

count = 0
i = 0
while i < N:
    j = i + 1
    while j < N and a[j - 1] != a[j]:
        j += 1
    if j != N:
        count += 1
    i = j + 1

print(count)
