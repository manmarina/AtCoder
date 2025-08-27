X, Y = map(int, input().split())

# 必要十分条件は：Y が偶数（整数解条件） 2X ≤ Y ≤ 4X（非負条件）
ok = (Y % 2 == 0) and (2 * X <= Y <= 4 * X)
print("Yes" if ok else "No")
