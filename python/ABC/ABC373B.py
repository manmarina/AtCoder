S = input()

ans = 0
for i in range(65, 90):
    cur = chr(i)
    nex = chr(i + 1)
    # print(cur, nex)

    icur = S.find(cur)
    inex = S.find(nex)
    # print(icur, inex)

    ans += abs(inex - icur)
print(ans)
