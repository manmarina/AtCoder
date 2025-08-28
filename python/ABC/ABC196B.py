X = input()

num = X.find('.')
if num == -1:
    print(X)
else:
    print(X[:num])
