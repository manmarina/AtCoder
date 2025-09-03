N, X = map(int, input().split())
A = list(map(int, input().split()))

for i in range(100 + 1):
    temp = A.copy()
    temp.append(i)
    sm = sum(temp) - max(temp) - min(temp)
    if sm >= X:
        print(i)
        break
else:
    print(-1)
