N = int(input())

a = [int(input()) for i in range(N)]
# print(a)

count = 1
i = 0
while count < N:
    if a[i] == 2:
        print(count)
        break
    i = a[i] - 1
    count += 1
else:
    print(-1)
