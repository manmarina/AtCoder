x = int(input())

div = x // 11
mod = x % 11
rem = 0
if 0 < mod <= 6:
    rem = 1
elif mod > 6:
    rem = 2

print(div * 2 + rem)
