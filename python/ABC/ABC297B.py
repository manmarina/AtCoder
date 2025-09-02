S = input()

Bi = [i for i, s in enumerate(S) if s == 'B']
Ri = [i for i, s in enumerate(S) if s == 'R']
# print(Bi)
# print(Ri)

ok_B = Bi[0] % 2 != Bi[1] % 2
ok_R = Ri[0] < S.index('K') < Ri[1]

print("Yes" if ok_B and ok_R else "No")
