S = input()

nl = []
for i in range(len(S) - 2):
    nl.append(int(S[i:i + 3]))

# print(nl)

dif = []
for num in nl:
    dif.append(abs(753 - num))

# print(dif)

print(min(dif))
