S = [input() for _ in range(8)]

# print(S)
# l = str.maketrans({'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e', '5': 'f', '6': 'g', '7': 'h'})
l = str.maketrans('01234567', 'abcdefgh')
r = str.maketrans('76543210', '12345678')

for i in range(8):
    for j in range(8):
        if S[i][j] == '*':
            c = str(j).translate(l)
            r = str(i).translate(r)
            print(c + r)
            exit()
