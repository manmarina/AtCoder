S = input()

ln = len(S)
for i in range(ln, 0, -1):
    for j in range(ln - i + 1):
        sec = S[j:j + i]
        if sec == sec[::-1]:
            # print(sec)
            print(len(sec))
            exit()
