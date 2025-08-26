N, M, X, Y = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

L = max(x)
R = min(y)
for i in range(X + 1, Y + 1):
    if L < i <= R:
        print("No War")
        break
else:
    print("War")
