X = int(input())

total = 0
for i in range(1, 9 + 1):
    for j in range(1, 9 + 1):
        ij = i * j
        if ij != X:
            total += ij
print(total)
