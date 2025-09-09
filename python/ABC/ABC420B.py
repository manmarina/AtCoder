N, M = map(int, input().split())
S = [input().strip() for _ in range(N)]

score = [0] * N
for j in range(M):
    cnt1 = sum(S[i][j] == '1' for i in range(N))
    cnt0 = N - cnt1
    if cnt0 == 0 or cnt1 == 0:
        # 全員 +1
        for i in range(N):
            score[i] += 1
    else:
        # 少数派だけ +1
        minority = '0' if cnt0 < cnt1 else '1'
        for i in range(N):
            if S[i][j] == minority:
                score[i] += 1

mx = max(score)
ans = [str(i + 1) for i, v in enumerate(score) if v == mx]
print(" ".join(ans))
