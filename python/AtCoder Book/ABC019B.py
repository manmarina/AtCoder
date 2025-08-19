S = input()

comp = []
i = 0
while i < len(S):
    j = i + 1
    while j < len(S) and S[j] == S[i]:
        j += 1
    comp.append(S[i] + str(j - i))
    i = j

print(*comp, sep='')
