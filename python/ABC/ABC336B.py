N = int(input())

b = bin(N)               # '0b...'
print(len(b) - len(b.rstrip('0')))
