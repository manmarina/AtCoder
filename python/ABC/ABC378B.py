N = int(input())
q, r = [], []
for _ in range(N):
    qi, ri = map(int, input().split())
    q.append(qi)
    r.append(ri)

Q = int(input())
td = [list(map(int, input().split())) for _ in range(Q)]

for t, d in td:
    t -= 1

    # x = d + (r - d % q + q) % q という余り合わせの実用公式
    delta = (r[t] - d % q[t] + q[t]) % q[t]
    print(d + delta)
