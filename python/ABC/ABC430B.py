N, M = map(int, input().split())
S = [input() for _ in range(N)]
# print(S)

check = set()
for j in range(N - M + 1):
    # print('j', j)
    for i in range(N - M + 1):
        # print('i', i)
        temp = []
        for k in range(M):
            # print('k+i', k+i)
            # print(tuple(S[i+k][j:j+M]))
            temp.append(tuple(S[i + k][j:j + M]))
        check.add(tuple(temp))
# print(check)
print(len(check))
