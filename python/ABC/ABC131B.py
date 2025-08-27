N, L = map(int, input().split())

ans = []
for i in range(1, N + 1):
    ans.append(L + i - 1)

# print(ans)
print(sum(ans) - min(ans, key=abs))
