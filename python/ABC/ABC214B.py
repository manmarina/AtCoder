from itertools import product
from timeit import repeat
S, T = map(int, input().split())

count = 0
for a, b, c in product(range(S + 1), repeat=3):
    if a + b + c <= S and a * b * c <= T:
        # print((a, b, c))
        count += 1

print(count)
