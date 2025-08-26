from itertools import permutations

A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())


def ceil_to_tens(n):
    return ((n + 9) // 10) * 10


menu = [A, B, C, D, E]

total = sum(ceil_to_tens(v) for v in menu)
best = max((10 - (v % 10)) % 10 for v in menu)

# print(best)
# print(total)

print(total - best)
