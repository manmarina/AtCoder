A, B, C, X = map(int, input().split())

if X <= A:
    print(1)
elif X > B:
    print(0)
else:
    print(f"{C / (B - A):.12f}")
