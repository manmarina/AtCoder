N, M = map(int, input().split())
S = [input() for _ in range(N)]

votes = [z for z in zip(*S)]
# print(votes)

point = [0] * N
for vote in votes:
    cnt1 = sum(v == '1' for v in vote)
    cnt0 = len(vote) - cnt1
    # print(cnt1, cnt0)

    if cnt1 == 0 or cnt0 == 0:
        for i in range(N):
            point[i] += 1
    else:
        minority = '0' if cnt0 < cnt1 else '1'
        for i in range(N):
            if vote[i] == minority:
                point[i] += 1

print(*[i + 1 for i, p in enumerate(point) if p == max(point)])
