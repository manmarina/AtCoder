N, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
sm = sum(A[1:-1])

# print(A)
# print(sm)

if N == 3:
    if A[0] >= X:
        print(0)
        exit()
    elif A[1] >= X:
        print(A[1])
        exit()
    else:
        print(-1)
        exit()

need = X - sm
if need <= 0:
    print(0)
elif need <= 100:
    print(need)
else:
    print(-1)
