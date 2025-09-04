N, L, R = map(int, input().split())
A = list(map(int, input().split()))

ans = []
for a in A:
    value = []
    LtoR = []
    for i in range(L, R + 1):
        value.append(abs(i - a))
        LtoR.append(i)
    # print(value, LR)
    ans.append(LtoR[value.index(min(value))])
print(*ans)
