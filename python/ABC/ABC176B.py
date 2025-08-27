N = input()

num = 0
for n in N:
    num += int(n)

if num % 9 == 0:
    print("Yes")
else:
    print("No")
