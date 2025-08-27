N = int(input())

ok = {i * j for i in range(1, 9 + 1) for j in range(1, 9 + 1)}
print("Yes" if N in ok else "No")
