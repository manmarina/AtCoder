S = input()

cen = len(S) // 2
L = S[:cen]
R = S[:-(cen + 1):-1]

# print(L, R)
count = 0
for i in range(cen):
    if L[i] != R[i]:
        count += 1
print(count)
