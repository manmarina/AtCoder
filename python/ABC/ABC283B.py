N = int(input())
A = [0] + list(map(int, input().split()))
Q = int(input())
ql = [list(map(int, input().split())) for _ in range(Q)]

# print(A)
# print(ql)

for q in ql:
    if q[0] == 1:
        A[q[1]] = q[2]
    else:  # q[0] == 2
        print(A[q[1]])
