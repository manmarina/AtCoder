X = int(input())


def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f


for i in range(2, 20 + 1):
    f = factorial(i)
    if f == X:
        print(i)
        break
