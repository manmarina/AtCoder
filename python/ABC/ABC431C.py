N, M, K = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))

H.sort()
B.sort()
# print(H)
# print(B)

cnt = 0
k = 0
for i in range(N):
    while i + k < M and H[i] > B[i + k]:
        k += 1
    if i + k >= M:
        break
    # head = H[i]
    # body = B[i + k]
    cnt += 1
# print(k)
# print(cnt)
if cnt >= K:
    print("Yes")
else:
    print("No")

"""
AC
"""
