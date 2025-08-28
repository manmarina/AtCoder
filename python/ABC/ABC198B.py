N = input()

s = N.rstrip('0')

print("Yes" if s == s[::-1] else "No")
