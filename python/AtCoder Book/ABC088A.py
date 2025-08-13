N = int(input())
A = int(input())

mod = N % 500
if mod > A:
    print("No")
else:
    print("Yes")
