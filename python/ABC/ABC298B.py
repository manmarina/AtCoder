N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
# print(A)
# print(B)


def rotate(A):
    return [list(row) for row in zip(*A[::-1])]

# 3重ループの内側の2重ループから一発で抜けるために関数化


def ok(A, B):
    for i in range(N):
        for j in range(N):
            if A[i][j] == 1 and B[i][j] != 1:
                return False
    return True


for _ in range(4):
    if ok(A, B):
        print("Yes")
        break
    A = rotate(A)
    # print(rotate(A))
else:
    print("No")
