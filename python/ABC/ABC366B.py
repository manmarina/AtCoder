N = int(input())
S = [input() for _ in range(N)]
# print(S)

mx = max([len(s) for s in S])
# print(mx)

hor = []
for s in S:
    hor.append(s + '*' * (mx - len(s)))
# print(hor)

ver = [''.join(list(h)) for h in zip(*hor[::-1])]
# print(ver)

ver = [v.rstrip('*') for v in ver]
# print(ver)
print(*ver, sep='\n')
