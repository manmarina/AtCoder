N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

# print(S)
# print(T)

ok = set(T)
# print(ok)

count = 0
for s in S:
    if s[3:] in ok:
        count += 1
print(count)
