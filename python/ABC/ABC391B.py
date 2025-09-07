N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]
# print(S)
# print(T)

for i in range(N - M + 1):
    for j in range(N - M + 1):
        if all(S[i + k][j + l] == T[k][l] for k in range(M) for l in range(M)):
            print(i + 1, j + 1)
            break
