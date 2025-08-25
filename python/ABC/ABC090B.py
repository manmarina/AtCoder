A, B = map(int, input().split())

ans = 0
for num in range(A, B + 1):
    half = len(str(num)) // 2
    pre = str(num)[:half]
    suf = str(num)[:-half - 1:-1]
    if pre == suf:
        ans += 1
print(ans)
