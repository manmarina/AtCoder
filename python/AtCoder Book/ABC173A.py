A = int(input())

change = 0
if A % 1000:
    pay = (A // 1000 + 1) * 1000
    change = pay - A

print(change)
