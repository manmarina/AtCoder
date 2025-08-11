A, B = map(int, input().split())

if A > B:
    print("No")
elif A*6 >= B:
    print("Yes")
else:
    print("No")
