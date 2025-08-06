S = list(map(int, input().split()))
S.sort()

if (S[0] == S[1] and S[2] == S[3] == S[4]) or (S[0] == S[1] == S[2] and S[3] == S[4]):
    print("Yes")
else:
    print("No")
