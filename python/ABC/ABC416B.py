S = input()

used = False
T = []
for s in S:
    if s == '#':
        T.append('#')
        used = False
    else:  # S == '.'
        if not used:
            T.append('o')
            used = True
        else:
            T.append(".")
print(*T, sep='')
