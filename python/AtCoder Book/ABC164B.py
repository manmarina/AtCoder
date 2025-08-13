A, B, C, D = map(int, input().split())

flag = 1
while A > 0 and C > 0:
    if flag % 2:
        C -= B
    else:
        A -= D
    flag += 1

print("Yes" if A > 0 else "No")
