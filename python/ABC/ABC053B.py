S = input()

l = S.find('A')
r = S.rfind('Z') + 1
print(len(S[l:r]))
