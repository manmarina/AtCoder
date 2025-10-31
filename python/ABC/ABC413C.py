Q = int(input())
A = []
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        _, c, x = q
        for _ in range(c):
            A.append(x)
    else:  # q[0] == 2:
        _, k = q
        print(sum(A[:k]))
        A = A[k:]

"""
TLE
"""
