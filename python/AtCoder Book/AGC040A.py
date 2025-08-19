S = input().strip()
N = len(S)

L = [0] * (N + 1)
for i, c in enumerate(S):
    if c == '<':
        L[i + 1] = L[i] + 1
print(L)

R = [0] * (N + 1)
for i in range(N - 1, -1, -1):
    if S[i] == '>':
        R[i] = R[i + 1] + 1
print(R)
print(list(map(max, zip(L, R))))

print(sum(max(L[i], R[i]) for i in range(N + 1)))
