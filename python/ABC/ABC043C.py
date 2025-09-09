N = int(input())
A = list(map(int, input().split()))

mn, mx = min(A), max(A)
ans = []
for i in range(mn, mx + 1):
    cost = 0
    for a in A:
        cost += (a - i)**2
    ans.append(cost)
print(min(ans))
