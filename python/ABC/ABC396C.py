N, M = map(int, input().split())
B = list(map(int, input().split()))
W = list(map(int, input().split()))

B.sort(reverse=True)
W.sort(reverse=True)
# print("B:", B)
# print("W:", W)

Bt = 0
i = 0
for i in range(N):
    if B[i] >= 0:
        Bt += B[i]
    else:
        break
# print("Bt:", Bt, "i:", i)

Wt = 0
j = 0
for j in range(i):  # range(i)がポイント！
    if W[j] >= 0:
        Wt += W[j]
    else:
        break
j += 1
# print("Wt:", Wt, "j:", j)

while i < N and j < M and W[j] + B[i] >= 0:
    Bt += B[i]
    Wt += W[j]
    i += 1
    j += 1
# print("Bt:", Bt, "i:", i)
# print("Wt:", Wt, "j:", j)

print(Bt + Wt)

"""
TLE & WA
"""
