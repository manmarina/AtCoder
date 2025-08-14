import math

N, D = map(int, input().split())
XY = []
for i in range(N):
    XY.append(list(map(int, input().split())))

# print(XY)

distance = [math.sqrt(x**2 + y**2) for x, y in XY]
# distance = list(map(lambda xy: math.sqrt(xy[0]**2 + xy[1]**2), XY))
# print(distance)

count = sum(d <= D for d in distance)
print(count)
