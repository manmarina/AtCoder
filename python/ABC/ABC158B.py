N, A, B = map(int, input().split())

full = N // (A + B)
rem = N % (A + B)
blue = full * A + min(rem, A)

print(blue)
