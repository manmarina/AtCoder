from math import sqrt

N = int(input())
x = list(map(int, input().split()))

manhattan = sum(abs(v) for v in x)

euclidean = sqrt(sum(v**2 for v in x))

chebyshev = max(abs(v) for v in x)

print(manhattan)
print(euclidean)
print(chebyshev)
