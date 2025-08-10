A, B, C = map(int, input().split())

ans = -1
calc = C * ((A // C) + 1)
if A % C == 0:
    ans = A
elif A <= calc <= B:
    ans = calc

print(ans)
