N = int(input())

a = [int(input()) for i in range(N)]
print(a)

count = 1
i = 0
visited = []
while 1:
    if i in visited:
        print(-1)
        break
    if a[i] == 2:
        print(count)
        break
    visited.append(i)
    i = a[i] - 1
    count += 1
