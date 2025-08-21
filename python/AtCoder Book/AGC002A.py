a, b = map(int, input().split())

if a == 0 or b == 0:
    print("Zero")
elif a > 0:
    print("Positive")
elif b < 0:
    if (-a - -b) % 2 == 0:
        print("Negative")
    else:
        print("Positive")
else:
    print("Zero")
