S = input()
T = input()

Tset = set(T)
for i in range(1, len(S)):
    if S[i].isupper() and S[i - 1] not in Tset:
        print("No")
        break
else:
    print("Yes")
