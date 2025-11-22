from bisect import bisect_left


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()
# print(A)
# print(B)

if min(A) > max(B):
    print(max(B) + 1)
    exit()

for i in range(N):
    seller = i + 1
    idx = bisect_left(B, A[i])
    buyer = M - idx
    print(A[i], "seller:", seller, "buyer:", buyer)
    if seller >= buyer:
        print(A[i])
        exit()

print(max(B) + 1)

"""
WA
"""
