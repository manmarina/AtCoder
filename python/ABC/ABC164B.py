A, B, C, D = map(int, input().split())

takahashi = True
while 1:
    if takahashi:
        C -= B
        takahashi = False
        if C <= 0:
            print("Yes")
            break
    else:
        A -= D
        takahashi = True
        if A <= 0:
            print(("No"))
            break
