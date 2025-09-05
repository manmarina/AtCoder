S = input()
T = input()

i = 0
ans = []
for j in range(len(T)):
    if T[j] == S[i]:
        ans.append(j + 1)
        i += 1
        if i == len(S):
            break

print(*ans)
