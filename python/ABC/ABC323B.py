N = int(input())
S = [input() for _ in range(N)]
# print(S)

ans = []
for i in range(N):
    count = 0
    for j in range(N):
        if S[i][j] == 'o':
            count += 1
    ans.append((i + 1, count))
# print(ans)

ans = sorted(ans, key=lambda x: (-x[1], x[0]))
print(*[i for i, r in ans])
