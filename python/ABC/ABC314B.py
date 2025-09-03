N = int(input())
A = []
for _ in range(N):
    _ = input()
    A.append(list(map(int, input().split())))
X = int(input())
# print(A)

result = []
for i, a in enumerate(A, 1):
    if X in a:
        result.append((i, len(a)))
# print(result)

if not result:
    print(0)
else:
    mn = min(r for _, r in result)
    ans = [i for i, r in result if r == mn]
    print(len(ans))
    print(*ans)
