import math

A, B, C = map(int, input().split())
print("YES" if C % math.gcd(A, B) == 0 else "NO")
