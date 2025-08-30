N = int(input())
S = [*input()]

# print(S)

if S[0] == 'A':
    ok = 'AB' * N
else:
    ok = 'BA' * N
ok = [*ok]

# print(ok)

count = 0
while 1:
    for i in range(N * 2 - 2):
        if S[i] == 'A' and S[i + 1] == 'A' and S[i + 2] == 'B':
            S[i + 1], S[i + 2] = S[i + 2], S[i + 1]
            count += 1

            # print(S)

            if S == ok:

                # print(S)

                print(count)
                exit()
            break

        if S[i] == 'B' and S[i + 1] == 'B' and S[i + 2] == 'A':
            S[i + 1], S[i + 2] = S[i + 2], S[i + 1]
            count += 1

            # print(S)

            if S == ok:

                # print(S)

                print(count)
                exit()
            break
