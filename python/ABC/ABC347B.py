s = input()

seen = set()
n = len(s)
for i in range(n):
    for j in range(i + 1, n + 1):
        print(i, j)
        seen.add(s[i:j])
print(len(seen))
