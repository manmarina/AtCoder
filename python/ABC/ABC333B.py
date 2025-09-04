S = input()
T = input()


def idx(ch):
    return ord(ch) - ord('A')


s1, s2 = idx(S[0]), idx(S[1])
t1, t2 = idx(T[0]), idx(T[1])
# print(s1, s2)
# print(t1, t2)

ds = min(abs(s1 - s2), 5 - abs(s1 - s2))
dt = min(abs(t1 - t2), 5 - abs(t1 - t2))
print("Yes" if ds == dt else "No")
