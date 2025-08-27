N = int(input())
p = list(map(int, input().split()))

mismatch = sum(i != v for i, v in enumerate(p, 1))
print("YES" if mismatch in (0, 2) else "NO")
