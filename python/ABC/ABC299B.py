N, T = map(int, input().split())
C = list(map(int, input().split()))
R = list(map(int, input().split()))

CR = [(c, r) for c, r in zip(C, R)]
# print(CR)

if T in C:
    print(R.index(max(r for c, r in CR if c == T)) + 1)
else:
    print(R.index(max(r for c, r in CR if c == C[0])) + 1)
