N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
# print(A)
# print(B)

ans = [False] * (N + 1)

while 1:
    changed = False
    for i in range(0, N):
        a = A[i]
        b = B[i]
        if ans[i + 1]:
            continue
        if a == 0 and b == 0:
            ans[i + 1] = True
            changed = True
            continue
        if ans[a] or ans[b]:
            ans[i + 1] = True
            changed = True
            continue
    else:
        if not changed:
            break

print(ans.count(True))
