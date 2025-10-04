from collections import defaultdict


S = input()

dd = defaultdict(int)
for s in S:
    dd[s] += 1
print(*[k for k, v in dd.items() if v == 1])
