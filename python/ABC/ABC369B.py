N = int(input())
AS = [list(input().split()) for _ in range(N)]
AS = [(int(a), s) for a, s in AS]
# print(AS)

lastL = None
lastR = None
ans = 0
for a, s in AS:
    if s == 'L':
        if lastL is not None:
            ans += abs(a - lastL)
        lastL = a
    else:  # s == 'R'
        if lastR is not None:
            ans += abs(a - lastR)
        lastR = a

print(ans)
