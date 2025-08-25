X = int(input())

ans = 1
for i in range(2, int(X**0.5) + 1):
    v = i
    while v <= X:
        if v > ans:
            ans = v
        v *= i
print(ans)
