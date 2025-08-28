P = list(map(int, input().split()))

# print(P)
print(*[chr(ord('a') + p - 1) for p in P], sep='')
