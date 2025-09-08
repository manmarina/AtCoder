N, Q = map(int, input().split())
X = list(map(int, input().split()))

cnt = [0] * (N + 1)
ans = []
for x in X:
    if x > 0:
        b = x
    else:  # x == 0のとき　「最小個数かつ最小番号」を毎回正しく選ぶ
        mn = 1
        for i in range(2, N + 1):
            if cnt[mn] > cnt[i]:
                mn = i
        b = mn
    cnt[b] += 1
    ans.append(b)
print(*ans)
