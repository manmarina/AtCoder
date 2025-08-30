X, Y = map(int, input().split())


def rev(num):
    num = str(num)[::-1]
    return int(num)


a = [0, X, Y]
for i in range(3, 10 + 1):
    x = a[i - 2]
    y = a[i - 1]

    a.append(rev(x + y))

print(a[-1])
