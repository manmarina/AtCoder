N = int(input())
S, T = input().split()

ans = []
for i in range(N):
    ans.append(S[i])
    ans.append(T[i])
print(*ans, sep='')
