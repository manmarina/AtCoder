S = input()

check = "AC"
if S[0] != 'A':
    check = "WA"
elif S[2:-1].count('C') != 1:
    check = "WA"
else:
    for i in range(len(S)):
        if i != 0 and i != S.index('C'):
            if not S[i].islower():
                check = "WA"
                break

print(check)
