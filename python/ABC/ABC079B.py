N = int(input())

L = [2, 1]
for i in range(2, 86 + 1):
    i = L[i - 1] + L[i - 2]
    L.append(i)

print(L[N])
