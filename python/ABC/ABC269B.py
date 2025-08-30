S = [input() for _ in range(10)]
# print(S)

# 左上
flag = False
for i in range(10):
    for j in range(10):
        if S[i][j] == '#':
            A = i + 1
            C = j + 1
            flag = True
            break
    if flag:
        break

# 右下
flag = False
for i in range(9, -1, -1):
    for j in range(9, -1, -1):
        if S[i][j] == '#':
            B = i + 1
            D = j + 1
            flag = True
            break
    if flag:
        break

print(A, B)
print(C, D)
