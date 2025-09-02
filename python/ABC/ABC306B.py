A = list(map(int, input().split()))

print(int(''.join(map(str, A[::-1])), 2))
