H, M = map(int, input().split())

if 5 < H < 10:
    H = 10
    M = 0
elif 15 < H < 20:
    H = 20
    M = 0

if 20 <= H <= 22 and M > 39:
    H += 1
    M = 0
elif H == 23 and M > 39:
    H = 0
    M = 0

print(H, M)
