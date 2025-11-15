X = int(input())

S = list(str(X))
S.sort()
# print(S)

if S[0] == '0':
    i = 0
    while S[i] == '0':
        i += 1
    S[0], S[i] = S[i], S[0]
    print(*S, sep='')
else:
    print(*S, sep='')
