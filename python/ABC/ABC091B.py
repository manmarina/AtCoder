from collections import defaultdict

N = int(input())
s = [input() for i in range(N)]
M = int(input())
t = [input() for i in range(M)]

# print(s)
# print(t)

dd = defaultdict(int)
for k in s:
    dd[k] += 1
for k in t:
    dd[k] -= 1
print(max(0, max(dd.values())))
