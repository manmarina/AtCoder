L, R = map(int, input().split())
S = input()

l = L - 1
r = R - 1

s = S[:l] + S[l:r + 1][::-1] + S[r + 1:]
print(s)
