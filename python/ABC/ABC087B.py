A = int(input())
B = int(input())
C = int(input())
X = int(input())

ans = 0
for i in range(A + 1):
    rem1 = X - 500 * i
    if rem1 < 0:
        break
    for j in range(min(B, rem1 // 100) + 1):
        rem2 = rem1 - 100 * j
        if rem2 % 50 == 0 and rem2 // 50 <= C:
            ans += 1
print(ans)
