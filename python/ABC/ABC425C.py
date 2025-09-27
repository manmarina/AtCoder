N, Q = map(int, input().split())
A = list(map(int, input().split()))
query = [list(map(int, input().split())) for _ in range(Q)]
# print(A)
# print(query)

cs = [0] + [A[0]]
for i in range(1, N):
    cs.append(cs[i] + A[i])
print(cs)

shift = 0
for q in query:
    if q[0] == 1:
        shift += q[1]
        print(shift)

    else:
        l = q[1] - 1 + shift
        r = q[2] + shift
        if l > N:
            l = l % N
            r = r % N
            print(cs[r] - cs[l] + A[N] * (r - l))
            # print(l, r)
        if r > N:
            ll = r % N
            r = N
            print(cs[r] - cs[l] + A[N] * (r - l))
            # print(l, r, ll)
        else:
            print(cs[r] - cs[l])
            # print(l, r)

        # print(cs[r] - cs[l])
