a, b, c, d = map(int, input().split())

prod = [a * c, a * d, b * c, b * d]
print(max(prod))
