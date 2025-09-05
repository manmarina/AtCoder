X = input()
# print(X)

X = X.rstrip('0')
# print(X)

if X.endswith('.'):
    X = X.rstrip('.')
print(X)
