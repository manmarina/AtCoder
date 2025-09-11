N, M, X = map(int, input().split())
C = []
A = []
for _ in range(N):
    row = list(map(int, input().split()))
    C.append(row[0])
    A.append(row[1:])

INF = 10**18
ans = INF

for mask in range(1 << N):
    cost = 0
    skill = [0] * M
    # 1) 本を積む
    for i in range(N):
        if (mask >> i) & 1:
            cost += C[i]
            if cost >= ans:  # 早期打ち切り
                break
            ai = A[i]
            for j in range(M):
                skill[j] += ai[j]
    else:
        # 2) しきい値判定（全て X 以上か）
        ok = True
        for j in range(M):
            if skill[j] < X:
                ok = False
                break
        if ok:
            # ans = min(ans, cost)
            ans = cost

print(ans if ans < INF else -1)
