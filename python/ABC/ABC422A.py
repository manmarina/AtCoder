S = input()

w = int(S[0])
s = int(S[2])
# print(w, s)
if s == 8:
    print(str(w + 1) + '-1')
else:
    print(str(w) + '-' + str(s + 1))
