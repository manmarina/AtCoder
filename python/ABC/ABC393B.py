S = input().strip()

n = len(S)
ans = 0
for j in range(n):
    if S[j] != 'B':
        continue
    lim = min(j, n - 1 - j)  # 右にも左にも d 進める最大
    for d in range(1, lim + 1):
        if S[j - d] == 'A' and S[j + d] == 'C':
            ans += 1
print(ans)
