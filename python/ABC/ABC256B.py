N = int(input())
A = list(map(int, input().split()))

base = [0, 0, 0, 0]

P = 0
for a in A:
    for b in (3, 2, 1):
        if base[b] == 1:
            base[b] = 0
            c = b + a
            if c > 3:
                P += 1
            else:
                base[c] = 1
    if a == 4:
        P += 1
    else:
        base[a] = 1

print(P)
