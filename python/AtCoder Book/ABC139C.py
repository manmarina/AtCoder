N = int(input())
H = list(map(int, input().split()))

count = 0
i = 0
while i < N:
    j = i + 1
    while j < N and H[j - 1] >= H[j]:
        j += 1
    temp = j - i - 1
    if temp > count:
        count = temp
    i = j

print(count)
