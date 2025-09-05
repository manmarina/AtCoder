S, T = input().split()

ls = len(S)
lt = len(T)
w = ls // lt
# print(w)

if w == ls:
    print("No")
    exit()

cut = []
for i in range(0, ls, w):
    cut.append(S[i:i + w])
# print(cut)

for j in range(w):
    temp = []
    for i in range(len(cut)):
        temp.append(cut[i][j:j + 1])
    temp = ''.join(temp)
    # print(temp)

    if temp == T:
        print("Yes")
        exit()
else:
    print("No")
