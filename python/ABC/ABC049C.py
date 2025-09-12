S = input()

words = ["dream", "dreamer", "erase", "eraser"]
while 1:
    for suf in words:
        if S.endswith(suf):
            S = S[:len(S) - len(suf)]

            # print(S)

            if len(S) == 0:
                print("YES")
                exit()
            else:
                break
    else:
        print("NO")
        exit()
