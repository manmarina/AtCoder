H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]
# print(A)

for row in A:
    temp = []
    for a in row:
        if a == 0:
            temp.append('.')
        else:
            temp.append(chr(ord('A') + a - 1))
    print(*temp, sep='')
