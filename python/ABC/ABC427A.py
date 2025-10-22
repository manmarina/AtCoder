S = list(input())

mid = (len(S) + 1) // 2 - 1
S.pop(mid)
print(*S, sep='')
