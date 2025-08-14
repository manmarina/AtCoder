N = int(input())
A = list(map(int, input().split()))

count = 0
while 1:
    for i in range(N):
        if A[i] % 2:
            print(count)
            exit()
        A[i] //= 2
    else:
        count += 1
