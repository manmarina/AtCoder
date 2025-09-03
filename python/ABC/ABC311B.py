N, D = map(int, input().split())
S = [input() for _ in range(N)]
# print(S)

count = 0
ans = [0] * D
for j in range(D):
    for i in range(N):
        if S[i][j] == 'x':
            count = 0
            break
    else:
        count += 1
        ans[j] = count
print(max(ans))
