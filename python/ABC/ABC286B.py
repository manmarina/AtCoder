N = int(input())
S = input()

ans = []
for i in range(N - 1):
    pair = S[i:i + 2]
    if pair == "na":
        ans.append("ny")
    else:
        ans.append(S[i])
ans.append(S[-1])
print(*ans, sep='')
