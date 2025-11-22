N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    for j in reversed(range(i)):
        # print(i, j)
        if A[i] < A[j]:
            print(j + 1)
            break
    else:
        print(-1)
