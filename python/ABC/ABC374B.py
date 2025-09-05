S = input()
T = input()

ls = len(S)
lt = len(T)

if ls > lt:
    T = T + '*'
elif ls < lt:
    S = S + '*'

for i in range(max(ls, lt)):
    if S[i] != T[i]:
        print(i + 1)
        break
else:
    print(0)
