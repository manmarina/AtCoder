N = int(input())
D = list(map(int, input().split()))

for i in range(N - 1):        # 0..N-2 が駅 i+1 を表す
    cur = 0
    row = []
    for j in range(i, N - 1):  # 区間 D_i..D_{j} を累積
        cur += D[j]
        row.append(str(cur))
    print(" ".join(row))
