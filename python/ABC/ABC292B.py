N, Q = map(int, input().split())
event = [list(map(int, input().split())) for _ in range(Q)]

# print(event)

player = [0] * (N + 1)
# print(player)

for e in event:
    i, x = e
    if i == 1:
        player[x] += 1
    elif i == 2:
        player[x] += 2
    else:  # i==3
        if player[x] >= 2:
            print("Yes")
        else:
            print("No")

# print(player)
