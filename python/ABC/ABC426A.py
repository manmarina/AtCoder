X, Y = input().split()

if X == "Ocelot":
    X = 1
elif X == "Serval":
    X = 2
else:
    X = 3

if Y == "Ocelot":
    Y = 1
elif Y == "Serval":
    Y = 2
else:
    Y = 3

print("Yes" if X >= Y else "No")
