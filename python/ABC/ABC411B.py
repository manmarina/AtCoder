N = int(input())
D = list(map(int, input().split()))

for i in range(N - 1):
    temp = []
    cs = 0
    for j in range(i, N - 1):
        cs += D[j]
        temp.append(cs)
    print(*temp)
