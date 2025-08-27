A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
b = set(int(input()) for _ in range(N))

# print(A)
# print(b)

X = [(0, 1, 2), (0, 1, 2), (0, 1, 2),
     (0, 0, 0), (1, 1, 1), (2, 2, 2),
     (0, 1, 2), (0, 1, 2)]
Y = [(0, 0, 0), (1, 1, 1), (2, 2, 2),
     (0, 1, 2), (0, 1, 2), (0, 1, 2),
     (0, 1, 2), (2, 1, 0)]

bingo = []
for xt, yt in zip(X, Y):
    temp = []
    for x, y in zip(xt, yt):
        temp.append(A[y][x])
    bingo.append(temp)

# print(bingo)

for line in bingo:
    # if set(line).issubset(b):
    if set(line) < b:
        print("Yes")
        break
else:
    print("No")
