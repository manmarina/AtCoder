N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

streak = 0
for d1, d2 in D:
    if d1 == d2:
        streak += 1
        if streak == 3:
            print("Yes")
            break
    else:
        streak = 0
else:
    print("No")
