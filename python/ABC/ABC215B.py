from math import log2

N = int(input())

k = int(log2(N))
if 2**(k + 1) <= N:
    k += 1
if 2**k > N:
    k -= 1
print(k)
