N = int(input())


def recursive(x):
    if (x == 1 or x == 0):
        return 1
    else:
        return x * recursive(x - 1)


print(recursive(N))
