N = int(input())
h = list(map(int, input().split()))

count = 0
i = 0
while i < N:
    j = i + 1
    while j < N and h[j - 1] <= h[j]:
        j += 1
    if j == N:
        count += h[j - 1]
    else:
        count += h[j - 1] - h[j]
    i = j


print(count)
