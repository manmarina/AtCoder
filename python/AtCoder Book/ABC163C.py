N = int(input())
A = list(map(int, input().split()))

G = [[] for i in range(N)]

for i, v in enumerate(A):
    i += 1
    v -= 1
    G[v].append(i)

print(*map(len, G), sep='\n')
