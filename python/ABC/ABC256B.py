N = int(input())
A = list(map(int, input().split()))

base = [0, 0, 0, 0]

P = 0
for a in A:
    if a == 1:
        if base[3] == 1:
            base[3] = 0
            P += 1
        if base[2] == 1:
            base[2] = 0
            base[3] = 1
        if base[1] == 1:
            base[1] = 0
            base[2] = 1
        base[1] = 1
    if a == 2:
        if base[3] == 1:
            base[3] = 0
            P += 1
        if base[2] == 1:
            base[2] = 0
            P += 1
        if base[1] == 1:
            base[1] = 0
            base[3] = 1
        base[2] = 1
    elif a == 3:
        if base[3] == 1:
            base[3] = 0
            P += 1
        if base[2] == 1:
            base[2] = 0
            P += 1
        if base[1] == 1:
            base[1] = 0
            P += 1
        base[3] = 1
    elif a == 4:
        if base[3] == 1:
            base[3] = 0
            P += 1
        if base[2] == 1:
            base[2] = 0
            P += 1
        if base[1] == 1:
            base[1] = 0
            P += 1
        P += 1
print(P)
