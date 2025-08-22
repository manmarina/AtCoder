N = int(input().strip())
S = input().strip()

x = 0
ans = 0  # 初期状態の 0 を含める
for ch in S:
    if ch == 'I':
        x += 1
    else:  # 'D'
        x -= 1
    if x > ans:
        ans = x

print(ans)
