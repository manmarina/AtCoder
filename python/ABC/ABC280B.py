N = int(input())
S = list(map(int, input().split()))
# print(S)

A = [S[0]]
for i in range(1, N):
    A.append(S[i] - S[i - 1])

print(*A)
