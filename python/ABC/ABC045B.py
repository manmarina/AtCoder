S = [[*input()] for i in range(3)]

# print(S)
card = 'a'
while 1:
    if card == 'a':
        if S[0]:
            card = S[0].pop(0)
        else:
            print('A')
            break
    elif card == 'b':
        if S[1]:
            card = S[1].pop(0)
        else:
            print('B')
            break
    elif card == 'c':
        if S[2]:
            card = S[2].pop(0)
        else:
            print('C')
            break
