N, M, T = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(M)]

# print(XY)

time = T
i = 1
while time > 0:
    for a in A:
        time -= a
        if time < 0:
            print("No")
            exit()
        i += 1
        for x, y in XY:
            if i == x:
                time += y
        if i == N:
            print("Yes")
            exit()
