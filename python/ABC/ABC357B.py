S = input()

clow = sum(s.islower() for s in S)
cupp = len(S) - clow

if clow > cupp:
    print(S.lower())
else:
    print(S.upper())
