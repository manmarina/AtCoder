S = input()
T = input()

dif = [i for i in range(len(S)) if S[i] != T[i]]

# print(dif)

if len(dif) == 0:
    print("Yes")
elif len(dif) == 2:
    i, j = dif
    if j == i + 1 and S[i] == T[j] and S[j] == T[i]:
        print("Yes")
    else:
        print("No")
else:
    print("No")
