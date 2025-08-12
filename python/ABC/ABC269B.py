S = []
for i in range(10):
    s = input()
    S.append(s)

D = 10
flag = False
for i in range(10):
    for j in range(10):
        if S[i][j] == '#' and not flag:
            A = i + 1
            C = j + 1
            flag = True
        if S[i][j] == '.' and flag:
            D = j
            break
    if flag:
        break

B = 10
flag = False
for i in range(A, 10):
    for j in range(10):
        if S[i][j] == '#':
            break
    else:
        B = i
        flag = True
        break
    if flag:
        break

print(A, B)
print(C, D)
