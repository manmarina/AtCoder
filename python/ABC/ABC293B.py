N = int(input())
A = list(map(int, input().split()))

called = [False] * (N + 1)
for i, a in enumerate(A, 1):
    if not called[i]:
        called[a] = True
# print(called)
ans = [i for i, c in enumerate(called) if c == False and i != 0]
print(len(ans))
print(*ans)
