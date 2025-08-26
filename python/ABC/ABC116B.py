s = int(input())

bin = {s}
count = 2
num = s
while 1:
    if num % 2 == 0:
        num //= 2
    else:
        num = 3 * num + 1
    if num in bin:
        print(count)
        break
    bin.add(num)
    count += 1
