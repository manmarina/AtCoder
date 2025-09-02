N, M = map(int, input().split())
C = list(input().split())
D = list(input().split())
P = list(map(int, input().split()))

default = P[0]
menu = dict(zip(D, P[1:]))
total = sum(menu.get(c, default) for c in C)
print(total)
