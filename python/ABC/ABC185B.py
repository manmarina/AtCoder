N, M, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(M)]

# print(AB)

bat = N
pre = 0
for i, o in AB:
    if bat <= i - pre:
        print("No")
        break
    bat -= i - pre
    bat = min(N, bat + o - i)
    pre = o
else:
    if bat <= T - pre:
        print("No")
    else:
        print("Yes")
