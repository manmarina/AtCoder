N, Q = map(int, input().split())
A = list(map(int, input().split()))
query = [list(map(int, input().split())) for _ in range(Q)]
# print(A)
# print(query)

cs = [0] + [A[0]]
for i in range(1, N):
    cs.append(cs[i] + A[i])
# print(cs)

for q in query:
    if q[0] == 1:
        A = A[q[1]:] + A[:q[1]]
        # print(A)

        cs = [0] + [A[0]]
        for i in range(1, N):
            cs.append(cs[i] + A[i])
        # print(cs)

    else:
        print(cs[q[2]] - cs[q[1] - 1])
