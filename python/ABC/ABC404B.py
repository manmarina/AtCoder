N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]


def rotate(S):
    s = [''.join(s) for s in zip(*S[::-1])]
    return s


ans = []
for k in range(4):
    # print(*S, sep='\n')
    # print()

    # print(*T, sep='\n')
    # print()
    count = 0
    for i in range(N):
        for j in range(N):
            if S[i][j] != T[i][j]:
                count += 1

    ans.append(count + k)

    if k < 3:
        S = rotate(S)

print(min(ans))
