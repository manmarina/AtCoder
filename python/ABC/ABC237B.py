H, W = map(int, input().split())
A = [list(map(int, input().split()))for _ in range(H)]
# print(A)

B = []
for a in zip(*A):
    B.append(a)
for b in B:
    print(*b)
