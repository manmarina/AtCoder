p, q = input().split()

d = [3, 1, 4, 1, 5, 9]
i, j = sorted([ord(p) - ord('A'), ord(q) - ord('A')])
print(sum(d[i:j]))
