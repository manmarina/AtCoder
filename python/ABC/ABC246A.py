X = [0, 0, 0]
Y = [0, 0, 0]

for i in range(3):
    X[i], Y[i] = map(int, input().split())

X3 = [i for i in X if X.count(i) == 1]
Y3 = [i for i in Y if Y.count(i) == 1]

print(*X3, *Y3)
