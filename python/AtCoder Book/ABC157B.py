A = []
for i in range(3):
    A.append(list(map(int, input().split())))
N = int(input())
B = []
for i in range(N):
    B.append(int(input()))

# print(A)
# print(B)


def make_bingos(matrix):
    Y = [[0, 0, 0], [1, 1, 1], [2, 2, 2],
         [0, 1, 2], [0, 1, 2], [0, 1, 2],
         [0, 1, 2], [2, 1, 0]]
    X = [[0, 1, 2], [0, 1, 2], [0, 1, 2],
         [0, 0, 0], [1, 1, 1], [2, 2, 2],
         [0, 1, 2], [0, 1, 2]]
    bingos = []
    for Y, X in zip(Y, X):
        bingo = []
        for y, x in zip(Y, X):
            bingo.append(matrix[y][x])
        bingos.append(bingo)
    return bingos


def is_bingo(bingos, select):
    for bingo in bingos:
        if set(bingo).issubset(select):
            return True
    return False


bingos = make_bingos(A)
# print(bingos)

print("Yes" if is_bingo(bingos, B) else "No")
