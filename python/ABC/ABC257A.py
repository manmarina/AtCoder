N, X = map(int, input().split())

index = 65 + X // N + (1 if X % N else 0) - 1
print(chr(index))
