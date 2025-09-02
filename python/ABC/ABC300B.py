H, W = map(int, input().split())
A = [[*input()] for _ in range(H)]
B = [[*input()] for _ in range(H)]
# print(A)
# print(B)


def shift_W(A):
    for row in A:
        last = row.pop()
        row.insert(0, last)
    return A


def shift_H(A):
    last = A.pop()
    A.insert(0, last)
    return A


for _ in range(H):
    for _ in range(W):
        if A == B:
            print("Yes")
            exit()
        shift_W(A)
    shift_H(A)
print("No")
