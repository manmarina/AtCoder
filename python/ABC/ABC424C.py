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
idx = set(i for i in range(N))
# print(idx)


def scan(i):
    a = A[i]
    b = B[i]
    if ans[i + 1]:
        idx.discard(i)
        return
    if a == 0 and b == 0:
        idx.discard(i)
        ans[i + 1] = True
        return
    if ans[a] or ans[b]:
        idx.discard(i)
        ans[i + 1] = True
        return


for i in range(0, N):
    scan(i)

while 1:
    idx2 = idx.copy()
    for i in idx:
        scan(i)
    if idx2 == idx:
        break

# print(idx)
print(ans.count(True))
