N = int(input())
S = [input().strip() for _ in range(N)]
T = [input().strip() for _ in range(N)]

diff = [0, 0, 0, 0]
for i in range(N):
    for j in range(N):
        # 0°
        diff[0] += (S[i][j] != T[i][j])
        # 90°
        diff[1] += (S[i][j] != T[j][N - 1 - i])
        # 180°
        diff[2] += (S[i][j] != T[N - 1 - i][N - 1 - j])
        # 270°
        diff[3] += (S[i][j] != T[N - 1 - j][i])

ans = min(diff[k] + k for k in range(4))
print(ans)
