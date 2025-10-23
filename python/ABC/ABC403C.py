N, M, Q = map(int, input().split())

perm = [set() for _ in range(N + 1)]

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        _, x, y = q
        perm[x].add(y)
    elif q[0] == 2:
        _, x = q
        for i in range(1, M + 1):
            perm[x].add(i)
    else:  # q[0] == 3
        _, x, y = q
        if y in perm[x]:
            print("Yes")
        else:
            print("No")

"""
TLE
"""
