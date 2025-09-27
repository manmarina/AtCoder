N, L, R = map(int, input().split())
S = input()

ok = (set(S[L - 1:R]) == {'o'})
print("Yes" if ok else "No")
