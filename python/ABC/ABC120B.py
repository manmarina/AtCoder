from math import gcd

A, B, K = map(int, input().split())

div = set()
num = gcd(A, B)

# print(num)

for i in range(1, int(num**0.5) + 1):
    if num % i == 0:
        div.add(i)
        div.add(num // i)
div = sorted(div)

# print(div)

print(div[-K])
