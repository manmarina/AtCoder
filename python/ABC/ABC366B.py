N = int(input())
S = [input().rstrip() for _ in range(N)]
M = max(len(s) for s in S)

for j in range(M):
    col = [(S[i][j] if j < len(S[i]) else '*') for i in range(N - 1, -1, -1)]
    print(''.join(col).rstrip('*'))
