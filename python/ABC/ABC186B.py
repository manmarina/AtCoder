H, W = map(int, input().split())
A = [x for _ in range(H) for x in map(int, input().split())]

# print(A)
# print(min(A))

ans = 0
for a in A:
    ans += a - min(A)
print(ans)
