from math import hypot

A, B = map(int, input().split())

r = hypot(A, B)
print(A / r, B / r)
