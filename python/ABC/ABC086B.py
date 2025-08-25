from math import isqrt

a, b = input().split()

num = int(a + b)
if num == isqrt(num)**2:
    print("Yes")
else:
    print("No")
