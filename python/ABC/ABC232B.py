S = input()
T = input()


def dif(ch1, ch2):
    return (ord(ch2) - ord(ch1)) % 26


ok = all(dif(S[i], S[i + 1]) == dif(T[i], T[i + 1]) for i in range(len(S) - 1))
print("Yes" if ok else "No")
