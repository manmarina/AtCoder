N, M, T = map(int, input().split())
A = [0]
A = A + list(map(int, input().split()))
X = []
Y = []
for i in range(M):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

# print(A)
# print(X)
# print(Y)

for i in range(1, N):
    T -= A[i]
    if i in X:
        T += Y[X.index(i)]
    if T <= 0:
        print("No")
        # print(T)
        break
else:
    print("Yes")
    # print(T)
