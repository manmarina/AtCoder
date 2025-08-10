XY = float(input())

Y = int((XY-int(XY))*10)
if Y < 3:
    sign = '-'
elif Y < 7:
    sign = ''
else:
    sign = "+"

print(str(int(XY))+sign)
