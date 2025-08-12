R, C = map(int, input().split())

dr = abs(R - 8)
dc = abs(C - 8)
d = dr if dr > dc else dc

if d % 2:
    print("black")
else:
    print("white")
