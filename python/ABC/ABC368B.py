N = int(input())
A = list(map(int, input().split()))

count = 0
while 1:
    A.sort(reverse=True)
    A[0] -= 1
    A[1] -= 1
    count += 1
    # print(A)
    if sum(1 for a in A if a > 0) <= 1:
        print(count)
        break
