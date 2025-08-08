a, b = map(int, input().split())

if abs(a - b) in (1, 9):
    print("Yes")
else:
    print("No")
