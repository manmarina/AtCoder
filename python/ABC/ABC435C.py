N = int(input())
A = list(map(int, input().split()))
# print(A)

i = 0
while i < N:
    hoge = i + A[i] - 1

    if hoge >= N - 1:
        print(N)
        exit()

    if A[hoge] == 1:
        print(hoge + 1)
        exit()

    i = hoge
