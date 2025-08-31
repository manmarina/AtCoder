from itertools import combinations

N, M = map(int, input().split())
S = [input() for _ in range(N)]

count = 0
for s1, s2 in combinations(S, 2):
    for c1, c2 in zip(s1, s2):
        if c1 == 'x' and c2 == 'x':
            break
    else:
        count += 1
print(count)
