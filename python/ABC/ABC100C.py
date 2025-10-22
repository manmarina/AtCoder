N = int(input())
A = list(map(int, input().split()))


cnt = 0
while not all(i % 2 == 1 for i in A):
    A.sort(reverse=True)
    flag = True
    for i in range(N):
        if flag and A[i] % 2 == 0:
            A[i] //= 2
            flag = False
        else:
            A[i] *= 3
    cnt += 1
# print(A)
print(cnt)
