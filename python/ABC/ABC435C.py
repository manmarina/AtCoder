N = int(input())
A = [0] + list(map(int, input().split()))
# print(A)

i = 1
while i <= N:
    hoge = i + A[i] - 1

    if hoge >= N:
        print(N)
        exit()

    max_ = i
    for j in range(i, hoge + 1):
        fuga = j + A[j] - 1
        max_ = max(max_, fuga)

    if max_ >= N:
        print(N)
        exit()

    if A[max_] == 1:
        print(max_)
        exit()

    i = max_

print(N)
