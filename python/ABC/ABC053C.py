X = int(input())
q, r = divmod(X, 11)
ans = 2 * q + (0 if r == 0 else 1 if r <= 6 else 2)
print(ans)
