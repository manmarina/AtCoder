S = input()

ok = all(s.islower() for s in S[::2]) and all(s.isupper() for s in S[1::2])
print("Yes" if ok else "No")
