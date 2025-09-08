S = input()

ls = len(S)
ans = 0
for i in range(ls - 2):
    # print(i)
    for j in range(i + 2, ls):
        # print(j, end=" ")
        # print(S[i:j + 1])
        s = S[i:j + 1]
        if s[0] == 't' and s[-1] == 't':
            ct = s.count('t')
            rate = (ct - 2) / (len(s) - 2)

            # print(s)
            # print(rate)

            ans = max(ans, rate)
print(ans)
