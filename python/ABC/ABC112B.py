N, T = map(int, input().split())
ct = [list(map(int, input().split())) for i in range(N)]

# print(ct)

cost = 1000
time = 1000
for c, t in ct:
    if t <= T:
        time = t
        if c < cost:
            cost = c

if time > T:
    print("TLE")
else:
    print(cost)
