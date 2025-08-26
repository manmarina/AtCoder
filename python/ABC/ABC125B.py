N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))

ans = []
for v, c in zip(V, C):
    premium = v - c
    if premium > 0:
        ans.append(premium)

print(sum(ans))
