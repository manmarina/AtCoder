S = [input() for _ in range(8)]

# print(S)

for i in range(8):
    for j in range(8):
        if S[i][j] == '*':
            r = str(8 - i)
            c = chr(ord('a') + j)
            print(c + r)
            exit()
