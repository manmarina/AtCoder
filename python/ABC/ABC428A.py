S, A, B, X = map(int, input().split())

ans = []
while X > 0:
    ans.append(S * min(A, X))
    X = X - A - B
# print(ans)
print(sum(ans))
