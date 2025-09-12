x = int(input())

res = (x // 11) * 2
r = x % 11
if r > 0:
    res += 1
if r > 6:
    res += 1
print(res)
