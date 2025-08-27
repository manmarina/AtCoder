N, A, B = map(int, input().split())

t = N // (A + B)
blue = t * A
rest = N - (A + B) * t

# print(blue)
# print(rest)

if rest > B:
    blue += B
else:
    blue += rest
print(blue)
