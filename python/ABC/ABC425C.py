N, Q = map(int, input().split())
A = list(map(int, input().split()))
query = [list(map(int, input().split())) for _ in range(Q)]
# print(A)
# print(query)

for q in query:
    if q[0] == 1:
        A = A[q[1]:] + A[:q[1]]
        # print(A)
    else:
        print(sum(A[q[1] - 1:q[2]]))
