N, K = map(int, input().split())

n = N
nl = []
while n > 0:
    nl.append(n % K)
    n //= K

# print(*nl[::-1], sep='')

print(len(nl))
