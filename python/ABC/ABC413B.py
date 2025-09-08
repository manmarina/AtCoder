from itertools import permutations

N = int(input())
S = [input() for _ in range(N)]

seen = set()
for s1, s2 in permutations(S, 2):
    s = s1 + s2
    seen.add(s)
print(len(seen))
